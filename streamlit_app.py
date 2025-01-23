import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="Text Classification", page_icon=":guardsman:", layout="wide")

# Load pre-trained models
with open('models/pipeline_bow.pkl', 'rb') as file:
    sentiment_model = pickle.load(file)

with open('models/sms_pipeline_bow.pkl', 'rb') as file:
    spam_model = pickle.load(file)

# Sidebar for selecting the type of prediction or information
option = st.sidebar.radio("Select a Task:", ("Sentiment Analysis", "Spam Detection", "About This Project"))

if option == "Sentiment Analysis":
    st.title("Review Sentiment Analysis")
    review = st.text_area("Enter Review Text:", "Type your review here...", height=200)
    
    if st.button("Predict Sentiment"):
        if review.strip():
            # Perform sentiment prediction
            prediction = sentiment_model.predict([review])
            sentiment = "Positive 😄" if prediction == 1 else "Negative 😞"
            st.subheader(f"Prediction: {sentiment}")
        else:
            st.error("Please enter a review before clicking the 'Predict' button.")

elif option == "Spam Detection":
    st.title("SMS Spam Detection")
    message = st.text_area("Enter SMS Text:", "Type your message here...", height=200)
    
    if st.button("Predict Spam"):
        if message.strip():
            # Perform spam detection
            prediction = spam_model.predict([message])
            classification = "Ham 📩" if prediction == 1 else "Spam 🚫"
            st.subheader(f"Prediction: {classification}")
        else:
            st.error("Please enter a message before clicking the 'Predict' button.")

elif option == "About This Project":
    st.title("About This Project")
    st.markdown("""
        ### Sentiment Analysis Model:
        This sentiment analysis model is built using different techniques:
        
        - **Bag of Words (BoW) with Multinomial Naive Bayes (MNB)**: This model achieved an accuracy of **85%** on the test dataset.
        - **TF-IDF (Term Frequency-Inverse Document Frequency)**: This model achieved an accuracy of **70%**.
        - **Average Word2Vec**: This model achieved an accuracy of **75%**.
        
        These models work by analyzing the text's content to classify whether the sentiment is **Positive** or **Negative**.

        ### Spam Detection Model:
        The spam detection model uses:
        
        - **Bag of Words (BoW) with Multinomial Naive Bayes (MNB)**: This model achieved an accuracy of **98%**.
        - **TF-IDF (Term Frequency-Inverse Document Frequency)**: This model achieved an accuracy of **97%**.
        - **Word2Vec**: This model achieved an accuracy of **94%**.

        This model classifies SMS messages as either **Spam** or **Ham** based on their content.

        **Note:** The performance of these models varies due to the different ways each technique captures the semantic meaning of the text.
    """, unsafe_allow_html=True)

    # Footer with your name
    st.markdown("""
        ---
        <p style="text-align:center; font-size:20px; color:#00bfff;">
            Made by <a href="https://github.com/prince2004patel" style="color:#00bfff; text-decoration:none;"><b>Prince Patel</b></a>
        </p>
    """, unsafe_allow_html=True)
