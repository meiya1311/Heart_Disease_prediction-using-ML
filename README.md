# Heart Disease Prediction Using Machine Learning

## 🔍 Project Overview

This project aims to develop a machine learning model to predict the presence of heart disease in patients based on various medical attributes. The model leverages the **Decision Tree Classifier** from scikit-learn and is trained on a publicly available heart disease dataset. The goal is to assist in early detection and diagnosis of heart-related conditions.

---

## 🧠 Model and Methodology

- **Algorithm Used:** Decision Tree Classifier (`sklearn.tree.DecisionTreeClassifier`)
- **Problem Type:** Binary Classification (1 = Disease Present, 0 = No Disease)
- **Evaluation Metrics:**
  - Accuracy Score
  - Precision, Recall, and F1-Score (via Classification Report)

---

## 📁 Dataset

- **File Name:** `heart.csv`
- **Features:**
  | Feature     | Description                                 |
  |-------------|---------------------------------------------|
  | age         | Age of the patient                          |
  | sex         | Gender (1 = male, 0 = female)               |
  | cp          | Chest pain type (4 values)                  |
  | trestbps    | Resting blood pressure                      |
  | chol        | Serum cholesterol (mg/dl)                   |
  | fbs         | Fasting blood sugar (> 120 mg/dl) (1/0)     |
  | restecg     | Resting electrocardiographic results        |
  | thalach     | Maximum heart rate achieved                 |
  | exang       | Exercise induced angina (1 = yes, 0 = no)   |
  | oldpeak     | ST depression induced by exercise           |
  | slope       | Slope of the peak exercise ST segment       |
  | ca          | Number of major vessels (0–3) colored       |
  | thal        | Thalassemia (3 = normal; 6 = fixed defect)  |
- **Target:** `target` (1 = disease, 0 = no disease)

---

## ⚙️ Implementation Steps

1. **Import Libraries**  
   Load essential Python libraries: `pandas`, `numpy`, `sklearn`.

2. **Load Dataset**  
   Read the dataset using `pandas.read_csv()` and separate features and target variable.

3. **Split the Dataset**  
   Use `train_test_split()` to divide the dataset into training and test sets (75% train, 25% test).

4. **Train the Model**  
   Instantiate and train a `DecisionTreeClassifier` using the training data.

5. **Make Predictions**  
   Predict on the test set and evaluate the performance using accuracy and a classification report.

6. **Real-Time Prediction**  
   Accept user input from the console and make predictions based on the trained model.

---

## 📊 Evaluation Results

- **Accuracy Score:** Printed on terminal after testing
- **Classification Report:** Includes precision, recall, F1-score for both classes

---

## 💬 Sample Usage

```bash
# Run the Python script
python heart_disease.py

# Enter input features when prompted
age= 52
sex= 1
cp= 0
...
thal= 2

# Sample Output
Predicted Output: 1  # (1 = Heart Disease Present)
```

---

## ✅ Future Improvements
- Integrate a **GUI using Tkinter** or **web app using Streamlit**
- Compare additional models such as **XGBoost**, **KNN**, or **Neural Networks**
- Apply **hyperparameter tuning** (e.g., GridSearchCV) for optimal performance
- Include more **data visualizations** and detailed **EDA**



## 🙋‍♀️ Author

**Meiyashini Nagarajan**  
- 📧 meiyashini1311@gmail.com  
- 🌐 [LinkedIn](https://www.linkedin.com/in/meiyashini-nagarajan)  
- 💻 [GitHub](https://github.com/meiya1311)

