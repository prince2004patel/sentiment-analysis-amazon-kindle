from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
with open('model/pipeline_bow.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json()  # Receive data as JSON
    review = data['reviewText']  # Extract review text
    
    # Make prediction using the model
    prediction = model.predict([review])
    
    sentiment = "Positive 😄" if prediction == 1 else "Negative 😞"
    return jsonify({"sentiment": sentiment})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
