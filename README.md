# 🏠 House Price Predictor with Linear Regression

A clean and beginner-friendly machine learning project that predicts house prices based on **area (sq.ft)**, **bedrooms**, and **bathrooms** using **Linear Regression**.

This project walks you through:
- Data preprocessing & splitting
- Model training, evaluation, and prediction
- Saving/loading model for reuse
- Plotting actual vs predicted prices
- Interactive CLI input from user

---

## 🧠 Tech Stack
- **Python 3.10+**
- `pandas`, `scikit-learn`, `joblib`
- `plotext` (for terminal plots) or `matplotlib`
- CLI interaction via `input()`

---

## 📁 Folder Structure
house-price-prediction-app/
│
├── data/ # Housing CSV dataset
├── models/ # Trained models (.pkl)
├── outputs/ # Predictions and plots
├── utils/ # Preprocessing logic
│ └── preprocessing.py
├── notebooks/ # EDA / Visualization
│ └── 01-eda.ipynb
├── main.py # Main pipeline script
├── requirements.txt # Install dependencies
└── README.md # Project documentation

---

## 🚀 How to Run It

### 1. 📦 Install Dependencies
```bash
pip install -r requirements.txt
python main.py

---


### 2. User Input Example

Enter house area (in sq.ft): 1600
Enter number of bedrooms: 3
Enter number of bathrooms: 2
Predicted Price: ₹315,000.00


---

## 🧾 README.md 

```markdown
---

## 📊 Output & Results

- Predictions saved to: `outputs/predictions.csv`
- Actual vs Predicted Plot:
  - Shown inline in terminal (via `plotext`)
  - Or saved as image (if using `matplotlib`)

---

## ✨ Features

- ✔️ Linear Regression with Scikit-Learn
- ✔️ Interactive user input for prediction
- ✔️ Plots rendered directly in the terminal
- ✔️ Clean modular folder structure
- ✔️ Beginner-friendly and production ready

---

## 📌 Sample Data Format (CSV)

```csv
Area,Bedrooms,Bathrooms,Price
1500,3,2,200000
1800,4,3,250000
...
