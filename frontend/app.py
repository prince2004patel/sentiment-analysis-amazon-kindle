import streamlit as st
import requests

# Set up the Streamlit page
st.set_page_config(page_title="Text Classification", page_icon=":guardsman:", layout="wide")

# Sidebar for selecting the type of prediction or information
option = st.sidebar.radio("Select a Task:", ("Sentiment Analysis", "Spam Detection", "About This Project"))

if option == "Sentiment Analysis":
    st.title("Review Sentiment Analysis")
    review = st.text_area("Enter Review Text:", "Type your review here...", height=200)
    
    if st.button("Predict Sentiment"):
        if review.strip():
            url = "http://127.0.0.1:5000/predict_sentiment"
            response = requests.post(url, json={"reviewText": review})
            
            if response.status_code == 200:
                result = response.json()
                st.subheader(f"Prediction: {result['sentiment']}")
            else:
                st.error("Failed to get prediction. Please try again.")
        else:
            st.error("Please enter a review before clicking the 'Predict' button.")

elif option == "Spam Detection":
    st.title("SMS Spam Detection")
    message = st.text_area("Enter SMS Text:", "Type your message here...", height=200)
    
    if st.button("Predict Spam"):
        if message.strip():
            url = "http://127.0.0.1:5000/predict_spam"
            response = requests.post(url, json={"messageText": message})
            
            if response.status_code == 200:
                result = response.json()
                st.subheader(f"Prediction: {result['classification']}")
            else:
                st.error("Failed to get prediction. Please try again.")
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
