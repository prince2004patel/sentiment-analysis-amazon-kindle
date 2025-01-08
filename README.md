# Sentiment Analysis on Amazon Kindle Dataset

## Best Practices (As suggested by Krish Naik)

### 1. Preprocessing and Cleaning

- **Text Cleaning**: Remove stop words, punctuation, special characters, and handle case sensitivity.
- **Tokenization**: Split the text into individual words (tokens).
- **Lemmatization**: Reduce words to their base or root form to improve uniformity.
- **Removing Duplicates**: Remove duplicate entries to avoid biases in model training.

### 2. Train Test Split

- **Data Split**: Split the dataset into a training set (typically 80%) and a test set (20%) to evaluate the model's performance on unseen data.

### 3. Feature Extraction: BOW, TF-IDF, Word2Vec

- **Bag of Words (BOW)**: Convert the text into a set of features based on word frequencies.
- **TF-IDF**: Weigh words based on their importance using term frequency and inverse document frequency.
- **Word2Vec**: Generate word vectors that capture semantic relationships between words.

### 4. Training ML Algorithms

- Start with simple and effective models like **Multinomial Naive Bayes (MNB)**, and explore other algorithms like **Support Vector Machines (SVM)**, **Logistic Regression**, or **Random Forest** for more complex tasks.

## Models Used

1. **Bag of Words (BoW) with Multinomial Naive Bayes (MNB)**

   - **Accuracy**: 85%
   - This model uses the Bag of Words approach to convert text into feature vectors and then classifies sentiments using Multinomial Naive Bayes.

2. **TF-IDF (Term Frequency-Inverse Document Frequency)**

   - **Accuracy**: 70%
   - TF-IDF evaluates the importance of words based on their frequency and inverse document frequency, and uses a machine learning classifier to predict sentiment.

3. **Average Word2Vec**
   - **Accuracy**: 75%
   - This model uses Word2Vec to convert words into vectors and averages the vectors to classify the sentiment of the text.

## Setup Instructions

### 1. Clone the Repository

To clone the repository, use the following command:

```bash
git clone https://github.com/your-username/sentiment-analysis-amazon-kindle.git
```

### 2. Install Dependencies

To install the required dependencies for this project, use the following command:

1. Ensure you are in the project directory:

```bash
cd sentiment-analysis-amazon-kindle
```

2. This will install all the necessary Python libraries required for both the Flask back-end and Streamlit front-end to work properly:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

1. Ensure you are in the project directory:

```bash
cd sentiment-analysis-amazon-kindle
```

2. Run the Flask application:

```bash
python app.py
```

3. Start the Streamlit app:

```bash
streamlit run app.py
```
