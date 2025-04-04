# 🏠 House Price Prediction using Machine Learning

This project focuses on predicting house prices using a Linear Regression model based on key property features. Built as part of a data science learning journey, it walks through the complete ML workflow—from data preprocessing to model evaluation.

## 📌 Project Objective

To develop a regression-based machine learning model that can accurately predict house prices based on various features such as area, number of bedrooms, and more.

## 📊 Dataset Overview

- The dataset consists of housing data including:
  - **Area**
  - **Number of Bedrooms**
  - **Number of Bathrooms**
  - **Parking Availability**
  - **Furnishing Status**
  - **City/Location**
  - **Price** (Target variable)

> Note: The dataset was cleaned and encoded manually within the notebook to handle categorical and missing data.

## 🧠 Machine Learning Workflow

1. **Data Loading & Exploration**
   - Used `pandas` for data handling.
   - Inspected data shape, types, and sample entries.

2. **Data Preprocessing**
   - Removed irrelevant columns.
   - Converted categorical data into numeric using `LabelEncoder`.
   - Handled missing values.

3. **Model Building**
   - Chose `LinearRegression` from `sklearn`.
   - Split data into training and test sets (80/20).
   - Trained the model and made predictions.

4. **Evaluation**
   - Compared actual vs predicted values.
   - Plotted results using `matplotlib` for visualization.
   - Calculated the R² Score to measure model accuracy.

## ⚙️ Tech Stack

- **Python**
- **Jupyter Notebook**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**

## 📈 Results

- The model gave a reasonable approximation of house prices.
- Simple Linear Regression performed well on the selected features.
- Visualization helped understand where the model under or over-predicts.

## 📁 How to Run

1. Clone this repository or download the notebook.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
