# 🧠 Real or Fake News Detection with BERT & Streamlit
https://github.com/rakesh-seerla1/projects/blob/main/Images/real%20&%20fake.png?raw=true

A machine learning web app to identify whether a piece of news is **real** or **fake**, using state-of-the-art NLP techniques. This project is built to **combat misinformation** in the digital era using **transformers** and deployed through **Streamlit** for real-time prediction.

---

## 🧩 Problem Statement

> **Fake news** is deliberately misleading information posing as legitimate news, often spread on social media. In an age where misinformation spreads faster than facts, there's an urgent need for automated tools to **detect fake news** reliably and efficiently.

This project provides a scalable and deployable solution that:
- Analyzes a news article using NLP
- Predicts whether the news is **Real** or **Fake**
- Presents an interactive interface for users to test and understand how such models work

---

## 🎯 Project Goals

- ✅ Build a robust NLP model using BERT
- ✅ Train the model on real and fake news data
- ✅ Analyze the dataset with visualizations
- ✅ Deploy the model using Streamlit
- ✅ Enable users to test live predictions via a clean interface

---

## 🚀 Live Demo

👉 **Try it here:** [https://fake-real-analysis-seerla.streamlit.app](https://fake-real-analysis-seerla.streamlit.app)

---

## 📂 Repository Structure Explained

Here’s a breakdown of every file/folder in the repo to help newcomers quickly understand:

| File / Folder | Purpose |
|---------------|---------|
| `app.py` | The main **Streamlit app** file. Runs the web interface. |
| `Research__Notebook.ipynb` | A **Jupyter notebook** with full EDA, model building, training, and evaluation code. Use this to understand the ML pipeline end-to-end. |
| `NLP_PROJECT_MODEL.pkl` | The **saved machine learning model** (BERT). Used by `app.py` to make predictions. |
| `tfidf_vectorization.pkl` | The **TF-IDF vectorizer** (used for baseline models). Optional legacy component. |
| `requirements.txt` | Python dependencies to run this project. |
| `sample_prediction.py` | Script to test predictions without using Streamlit (CLI-based version). |
| `SAMPLE DATA FROM TRUE AND FAKE DATASET.txt` | Contains sample inputs from the training dataset for testing. |
| `README.md` | This file — complete documentation of the project. |
| `images/` | Folder with screenshots and visualizations used in this README. |

---

## 🌐 Technologies Used

- **Python** 🐍
- **NLP / Transformers**: BERT (via Hugging Face)
- **Machine Learning**: Scikit-Learn
- **Web App**: Streamlit
- **EDA & Visualization**: Pandas, Seaborn, Matplotlib

---

## 🧠 How the Model Works

### 1. **Data Preprocessing**
- Clean and normalize text (remove punctuation, stopwords, etc.)
- Tokenize using BERT tokenizer

### 2. **Model Training**
- Fine-tuned **BERT** on labeled dataset of real/fake news
- Evaluated with accuracy, precision, recall, F1 score

### 3. **Prediction Pipeline**
- User inputs news text via Streamlit
- Text is tokenized and passed through the model
- Output is classified as **Real ✅** or **Fake ❌**

---

## 📊 Data Exploration & Visual Insights

### 🔸 Class Distribution (Real vs Fake)
Balanced dataset used to avoid model bias.

### 🔹 News Topics Distribution (Pie Chart)
![Pie Chart](images/Screenshot%202025-05-11%20142609.png)

### 🔹 Article Frequency by Topic
![Bar Chart](images/Screenshot%202025-05-11%20142621.png)

Insights:
- Majority articles are on **Politics**, **World News**, and **US News**
- This distribution shows where misinformation is most prevalent

---

## 🖼️ Streamlit App Walkthrough

### 🧪 Input Real News Example
![Real News Prediction](images/Screenshot%202025-05-11%20142013.png)

### 🚫 Input Fake News Example
![Fake News Prediction](images/Screenshot%202025-05-11%20142150.png)

---

## ⚙️ How to Run Locally

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/rakesh-seerla1/projects.git
cd projects
✅ Step 2: Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Step 3: Launch Streamlit app
bash
Copy
Edit
streamlit run app.py
🧪 Try Sample Data
Use the file SAMPLE DATA FROM TRUE AND FAKE DATASET.txt to copy-paste real examples into the app.

💡 Future Enhancements
🔍 Add explainability tools like SHAP or LIME

🌐 Expand dataset to multilingual fake news

📱 Create a mobile-friendly version

📡 Build API endpoints for integration

🙋‍♂️ Author
Rakesh Seerla
📧 seerlarakesh9160@gmail.com
🔗 LinkedIn - rakesh916
🐙 GitHub - rakesh-seerla1

🌟 Contributing
Pull requests and stars are welcome!
Feel free to fork this repo and submit improvements or ideas.

🏁 Final Note
This project demonstrates how AI can be used for social good — fighting disinformation with facts, algorithms, and open-source tools. Let’s build a safer internet together.

yaml
Copy
Edit

---

Would you like me to now:

1. 📁 Package this into a `README.md` file for download?
2. ⚙️ Help you commit it directly to your GitHub repo?
3. 🛠 Assist with renaming/uploading your images into your GitHub repo for proper linking?

Let me know how you'd like to proceed, bro.







