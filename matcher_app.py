import streamlit as st
import json
import spacy
import numpy as np
from scipy.spatial.distance import euclidean
st.set_page_config(page_title="Job and Resume Matching Application", layout="wide")

# Load spaCy model
nlp = spacy.load("en_core_web_lg")


# Load resumes and jobs
@st.cache_data
def load_data():
    with open("resumes.json") as f:
        resumes = json.load(f)
    with open("job_opportunities.json") as f:
        jobs = json.load(f)
    return resumes, jobs


resumes, jobs = load_data()


def get_mean_vector(keywords):
    vectors = []
    for word in keywords:
        token = nlp(word)
        if token.has_vector:
            vectors.append(token.vector)
    if vectors:
        return np.mean(vectors, axis=0)
    return np.zeros(nlp.vocab.vectors_length)


def find_top_matches(job_keywords, resumes, top_n=3):
    job_vec = get_mean_vector(job_keywords)
    scores = []
    for resume in resumes:
        res_vec = get_mean_vector(resume["key_words"])
        dist = euclidean(job_vec, res_vec)
        scores.append((resume, dist))
    scores.sort(key=lambda x: x[1])  # smaller = closer match
    return [res for res, _ in scores[:top_n]]


st.title("Job and Resume Mathing Application")

st.sidebar.title("Job Opportunities")

if 'selected_job_title' not in st.session_state:
    st.session_state.selected_job_title = None

for job in jobs:
    if st.sidebar.button(job["title"]):
        st.session_state.selected_job_title = job["title"]

# Main content
if st.session_state.selected_job_title:
    job = next((j for j in jobs if j["title"] == st.session_state.selected_job_title), None)

    if job:
        st.subheader(f"Job Opportunity: {job['title']}")
        st.markdown(f"**Key Words:**\n{', '.join(job['key_words'])}")
        st.markdown(f"**Description:**\n{job['text']}")


        top_matches = find_top_matches(job["key_words"], resumes)
        st.markdown("### Top 3 Matched Resumes:")

        job_vec = get_mean_vector(job["key_words"])  # For similarity calculation

        for match in top_matches:
            res_vec = get_mean_vector(match["key_words"])
            similarity_score = euclidean(job_vec, res_vec)

            resume_html = f"""
            <div style="background-color:#f0f0f0; padding:15px; border-radius:10px; margin-bottom:20px;">
                <h4>{match['title']}</h4>
                <p><strong>Similarity Score:</strong> {similarity_score:.2f}</p>
                <p><strong>Resume ID:</strong> {match.get('id', 'N/A')}</p>
                <p><strong>Keywords:</strong> {', '.join(match['key_words'])}</p>
                <p><strong>Description:</strong> {match.get('text', 'No description available.')}</p>
            </div>
            """
            st.markdown(resume_html, unsafe_allow_html=True)


    else:
        st.error("Selected job not found in data.")
else:
    st.info("Please select a job role from the left sidebar.")
