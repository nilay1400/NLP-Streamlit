
# 🧠 NLP Resume-to-Job Matcher (Practice Project)

This project allows you to match **job opportunities to resumes** using **spaCy embeddings** and **vector similarity**. It's a hands-on practice for those learning **NLP, vector embeddings**, and **basic UI development with Streamlit**.


## 🔍 Overview

Using `spaCy`'s `en_core_web_lg` language model, this app embeds **key words** from resumes and job descriptions. Users can:

- Select a **job** and view **top 3 matching resumes**
- The matching is calculated using **Euclidean distance** between vector means of keywords.

The project also introduces **basic data parsing from JSON**, **embedding aggregation**, and **Streamlit UI components** (such as buttons and markdown).


## 📁 Folder Structure

```plaintext
├── resumes.json
├── job_opportunities.json
└── matcher_app.py
````


## 📄 Deliverables

As part of this practice:

* Record a **30-second video** demonstrating your working app and how it responds to selections.
* Publish your code in a **public GitHub repository**.
* Share both the **GitHub link** and **video** in  **Telegram**.


## 🔗 Resources

* 🔗 [resumes.json](https://drive.google.com/file/d/1mLtCQ3jA6V9r5Eb5IqnL6ewZ6UaVg59O/view?usp=sharing)
* 🔗 [job\_opportunities.json](https://drive.google.com/file/d/1SJ5cL47dMMvBU2xVxwWbJHGsS0mzkV9t/view?usp=sharing)
* 🔗 [spaCy Documentation](https://spacy.io/usage/spacy-101)
* 🔗 [Streamlit Docs](https://docs.streamlit.io/)
