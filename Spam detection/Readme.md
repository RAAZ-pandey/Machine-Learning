# SMS Spam Detection using Machine Learning

## 📌 Project Overview
This project focuses on detecting spam messages in SMS texts using **machine learning** and **natural language processing (NLP)**. The goal is to classify messages as either "spam" or "ham" (not spam) based on their content.

## 📂 Contents
- **Data Preprocessing**: Cleaning and preparing SMS text data.
- **Feature Engineering**: Using techniques like **TF-IDF** and **Bag of Words** to extract meaningful features.
- **Model Training**: Implementing and evaluating multiple classification models:
  - Logistic Regression
  - Naïve Bayes
  - Random Forest
  - Support Vector Machine (SVM)
- **Performance Evaluation**: Using metrics such as **accuracy, precision, recall, and F1-score** to assess model effectiveness.

## 🚀 Technologies Used
- **Python**
- **Jupyter Notebook**
- **Scikit-learn** (for machine learning models)
- **NLTK** & **spaCy** (for text preprocessing)
- **Pandas & NumPy** (for data handling)
- **Matplotlib & Seaborn** (for visualization)

## 🔥 How to Use
1. Clone this repository:
   ```sh
   git clone <repo-link>
   cd sms-spam-detection
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:
   ```sh
   jupyter notebook sms-spam-detection.ipynb
   ```
4. Follow the notebook steps to train and evaluate the spam detection model.

## 📊 Results & Insights
- **Naïve Bayes** performed best due to its effectiveness in text classification.
- **TF-IDF** helped improve accuracy by focusing on important words.
- **Balancing data** helped in reducing bias towards non-spam messages.

## 💡 Future Enhancements
- Implement **deep learning models** like LSTMs for better accuracy.
- Deploy the model as an **API** for real-world applications.
- Improve feature extraction using **word embeddings (Word2Vec, BERT, etc.)**.

## 🤝 Let's Connect!
If you're interested in NLP, spam filtering, or machine learning projects, feel free to connect! 🚀

#MachineLearning #DataScience #NLP #SpamDetection #Python #TextClassification
