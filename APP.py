import os
import streamlit as st
import pickle

# Correct paths to model and vectorizer files using relative paths
model_path = "NLP_PROJECT_MODEL.pkl"
vectorizer_path = "tfidf_vectorization.pkl"

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

# Sidebar configuration
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an option:", 
                                ["Predict News", "Notebook", "Sample Data", "Contact Me"])

# Content based on selection
if option == "Predict News":
    st.title("Real or Fake News Analysis")
    user_input = st.text_area("Enter your text here:", key='user_input')

    # Button for prediction
    if st.button("Submit"):
        prediction = get_pred(st.session_state.user_input)
        st.write("Prediction: ", prediction)

elif option == "Notebook":
    st.title("REAL_or_FAKE_NEWS_ANALYSIS_PROJECT_NOTEBOOK")#https://github.com/rakesh-seerla1/projects/blob/main/REAL_or_FAKE_NEWS_ANALYSIS_PROJECT_NOTEBOOK.ipynb
    # Read and display the Jupyter Notebook content
    with open("NLP_REAL_or_FAKE_NEWS_ANALYSIS_PROJECT_NOTEBOOK.ipynb") as f:
        notebook_content = f.read()
    st.code(notebook_content, language='json')  # Display as code

elif option == "Sample Data":
    st.title("Sample Data")
    # Read and display the sample data
    with open("SAMPLE DATA FROM TRUE AND FAKE DATASET.txt") as f:
        sample_data_content = f.read()
    st.text_area("Sample Data", sample_data_content, height=300)

elif option == "Contact Me":
    st.title("Contact Me")
    st.write("For further queries or contact, please email me at:")
    st.write("**seerlarakesh9160@gmail.com**")

# Main app content
st.write("Use the sidebar to navigate through the options.")
