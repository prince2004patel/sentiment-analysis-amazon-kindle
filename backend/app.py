from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained models
with open('model/pipeline_bow.pkl', 'rb') as file:
    sentiment_model = pickle.load(file)

with open('model/sms_pipeline_bow.pkl', 'rb') as file:
    spam_model = pickle.load(file)

# Define a route for sentiment prediction
@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    review = data['reviewText']
    prediction = sentiment_model.predict([review])
    sentiment = "Positive 😄" if prediction == 1 else "Negative 😞"
    return jsonify({"sentiment": sentiment})

# Define a route for spam prediction
@app.route('/predict_spam', methods=['POST'])
def predict_spam():
    data = request.get_json()
    message = data['messageText']
    prediction = spam_model.predict([message])
    classification = "Ham 📩" if prediction == 1 else "Spam 🚫"
    return jsonify({"classification": classification})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
