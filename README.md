# 📰 Real or Fake News Detection using NLP and BERT

Welcome to the Real or Fake News Detection project — a robust and production-ready system that uses Natural Language Processing and Machine Learning to classify whether a given news article is **real** ✅ or **fake** ❌.

![Real vs Fake]
"C:\Users\seerl\Downloads\Portfolio-Website-Template-main\Portfolio-Website-Template-main\images\real & fake.png"



## 🔍 Overview

With the rise of fake news across social media, it's critical to validate information sources. This project:
- Uses a fine-tuned **BERT transformer model**
- Achieves over **99% accuracy**
- Is deployed using **Streamlit** for public use
- Includes a **notebook with data analysis and EDA**
- Allows users to test **live predictions**

---

## 📈 Visual Insights from the Dataset

### 🔹 Distribution of News Subjects
The dataset includes a variety of political and global news topics. Here’s the distribution:

![Distribution Pie](images/Screenshot%202025-05-11%20142609.png)

- **PoliticsNews (25.1%)**
- **WorldNews (22.4%)**
- **News (20.3%)**
- Smaller proportions from **US News**, **Middle East**, etc.

### 🔸 Frequency by Topic
Most articles fall under political and world news categories, often the ones most susceptible to fake news.

![Distribution Bar](images/Screenshot%202025-05-11%20142621.png)

---

## 💡 Features

- 🔍 Real-time Fake/Real News Detection
- 🧠 Fine-tuned BERT Model
- 📊 Visual EDA Insights
- 🌐 Streamlit App Interface
- 💾 Model and vectorizer stored with `.pkl`
- 🧪 Sample data for user testing

---

## 📲 Live App Demo

Try it here:  
👉 [Streamlit Web App](https://fake-real-analysis-seerla.streamlit.app)

---

## 🖼️ Interface Snapshots

### ✅ Prediction: Real News
![Prediction Real](images/Screenshot%202025-05-11%20141947.png)
![Prediction Real 2](images/Screenshot%202025-05-11%20142013.png)

### ❌ Prediction: Fake News
![Prediction Fake](images/Screenshot%202025-05-11%20142150.png)

---

## 📁 Project Structure

📦 Fake News Detection
├── app.py # Streamlit app
├── Research__Notebook.ipynb # Full data analysis & modeling
├── NLP_PROJECT_MODEL.pkl # Trained model
├── tfidf_vectorization.pkl # TF-IDF vectorizer
├── sample_prediction.py # Prediction logic for testing
├── requirements.txt # Dependencies
├── SAMPLE DATA FROM TRUE... # Testing data
├── images/ # Project visuals & screenshots
└── README.md

yaml
Copy
Edit

---

## 🧠 Model Summary

- Used **TF-IDF vectorization** for baseline and **transformers for final model**
- Fine-tuned **BERT** (110M parameters)
- Achieved **99.7% accuracy**
- Optimized for **text classification**

---

## 🖥️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/rakesh-seerla1/projects.git
   cd projects
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Launch the Streamlit app:

bash
Copy
Edit
streamlit run app.py
📂 Sample Data Format
The dataset contains labeled news articles:

vbnet
Copy
Edit
Label: 0 = REAL, 1 = FAKE

Text: "WASHINGTON (Reuters) - Transgender people will be allowed..."
📬 Contact Me
For any queries or feedback, reach out:

📧 Email: seerlarakesh9160@gmail.com
🔗 LinkedIn: linkedin.com/in/rakesh916
🐙 GitHub: github.com/rakesh-seerla1

🧭 Future Improvements
🧠 Integrate explainable AI (SHAP, LIME)

🌍 Add multilingual support

📱 Build a mobile-friendly version

✅ API support for third-party use

⭐ If you like this project, feel free to star the repo!

yaml
Copy
Edit

---

Let me know if you'd like me to create this as a downloadable `.md` file or help you automate the image upl
