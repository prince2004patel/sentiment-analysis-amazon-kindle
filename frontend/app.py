import streamlit as st
import requests

# Title and Introduction
st.set_page_config(page_title="Review Sentiment Analysis", page_icon=":guardsman:", layout="centered")
st.title("Review Sentiment Analysis")

# Review Input Section
review = st.text_area("Enter Review Text:", "Type your review here...", height=200)

# Predict button
if st.button("Predict"):
    if review.strip() != "":
        # Send review to the Flask backend
        url = "http://127.0.0.1:5000/predict"  # Flask local API endpoint
        response = requests.post(url, json={"reviewText": review})

        if response.status_code == 200:
            result = response.json()
            sentiment = result['sentiment']
            st.subheader(f"Prediction: {sentiment}")
        else:
            st.error("Failed to get prediction. Please try again.")
    else:
        st.error("Please enter a review before clicking the 'Predict' button.")

# Toggle button for "About the Model" section
if "show_about" not in st.session_state:
    st.session_state.show_about = False

if st.button("About the Model"):
    st.session_state.show_about = not st.session_state.show_about

if st.session_state.show_about:
    st.markdown("""
        ### About the Model:
        This sentiment analysis model is built using different techniques:
        
        - **Bag of Words (BoW) with Multinomial Naive Bayes (MNB)**: This model achieved an accuracy of **85%** on the test dataset.
        - **TF-IDF (Term Frequency-Inverse Document Frequency)**: This model achieved an accuracy of **70%**.
        - **Average Word2Vec**: This model achieved an accuracy of **75%**.

        These models work by analyzing the text's content to classify whether the sentiment is **Positive** or **Negative**.

        **Note:** The performance of the models varies due to the different ways each technique captures the semantic meaning of the text.
    """,unsafe_allow_html=True)


# Footer
st.markdown("""
    ---
    <p style="text-align:center; font-size:20px; color:#00bfff;">
        Made by <a href="https://github.com/prince2004patel" style="color:#00bfff; text-decoration:none;"><b>Prince Patel</b></a>
    </p>
""",unsafe_allow_html=True)
