import os
import streamlit as st
import pickle
import nbformat
from nbconvert import HTMLExporter

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
    return pred[0]  # Return the prediction directly

# Sidebar configuration
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an option:", 
                                ["Predict News", "Notebook", "Sample Data", "Contact Me"])

# Set a custom CSS style for the app
st.markdown("""
<style>
    .main {
        background-color: #f0f2f5;
        padding: 20px;
        border-radius: 10px;
    }
    .prediction-real {
        color: #28a745; /* Green */
        font-size: 24px;
        font-weight: bold;
    }
    .prediction-fake {
        color: #dc3545; /* Red */
        font-size: 24px;
        font-weight: bold;
    }
    .section-title {
        color: #007bff; /* Blue */
        font-size: 28px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Content based on selection
if option == "Predict News":
    st.title("Real or Fake News Analysis 📰")
    user_input = st.text_area("Enter your text here:", key='user_input')

    # Button for prediction
    if st.button("Submit"):
        prediction = get_pred(user_input)
        if prediction == 0:
            st.markdown("<div class='prediction-real'>✅ Prediction: Real News</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='prediction-fake'>❌ Prediction: Fake News</div>", unsafe_allow_html=True)

elif option == "Notebook":
    st.title("NLP Real or Fake News Analysis Notebook 📓")
    # Read and display the Jupyter Notebook content
    with open("REAL_or_FAKE_NEWS_ANALYSIS_PROJECT_NOTEBOOK.ipynb") as f:
        notebook_content = nbformat.read(f, as_version=4)
    
    # Convert notebook to HTML
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)
    
    # Display the notebook as HTML
    st.components.v1.html(body, height=800, scrolling=True)

elif option == "Sample Data":
    st.title("Sample Data 📊")
    # Read and display the sample data
    with open("SAMPLE DATA FROM TRUE AND FAKE DATASET.txt") as f:
        sample_data_content = f.read()
    st.text_area("Sample Data", sample_data_content, height=300)

elif option == "Contact Me":
    st.title("Contact Me 📧")
    st.write("For further queries or contact, please email me at:")
    st.write("**seerlarakesh9160@gmail.com**")

# Main app content
st.write("Use the sidebar to navigate through the options.")
