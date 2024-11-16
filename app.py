import os
import streamlit as st
import pickle

# Correct paths to model and vectorizer files
model_path = "C:/Users/seerl/OneDrive/Desktop/NLP_Project/NLP_PROJECT_MODEL.pkl"
vectorizer_path = "C:/Users/seerl/OneDrive/Desktop/NLP_Project/tfidf_vectorization.pkl"

# Ensure the paths are correct
assert os.path.exists(model_path), "Model file not found"
assert os.path.exists(vectorizer_path), "Vectorizer file not found"

# Load the model and vectorizer
loaded_model = pickle.load(open(model_path, "rb"))
loaded_tfidf = pickle.load(open(vectorizer_path, "rb"))

# Define prediction function
def get_pred(data):
    data = loaded_tfidf.transform([data])
    pred = loaded_model.predict(data)
    if pred == 0:
        return "Real News"
    else:
        return "Fake News"

# Streamlit app interface
st.title("Real or Fake News Analysis")

# Text input box
user_input = st.text_area("Enter your text here:", key='user_input')

# Button for prediction
if st.button("Submit"):
    prediction = get_pred(st.session_state.user_input)
    st.write("Prediction: ", prediction)
