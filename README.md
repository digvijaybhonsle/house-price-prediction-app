🏠 House Price Predictor with Linear Regression

A clean and beginner-friendly machine learning project that predicts house prices based on area (sq.ft), bedrooms, and bathrooms using Linear Regression.
This project guides you through:

Data preprocessing and train-test splitting
Training and evaluating a Linear Regression model
Saving and loading models for reuse
Visualizing actual vs. predicted prices
Interactive CLI for real-time predictions


🧠 Tech Stack

Python 3.10+
Libraries: pandas, scikit-learn, joblib
Visualization: plotext (terminal plots) or matplotlib (image output)
CLI interaction: Built-in input()


📁 Project Structure
house-price-prediction-app/
│
├── data/                 # Housing CSV dataset
├── models/               # Trained models (.pkl)
├── outputs/              # Predictions and plots
├── utils/                # Preprocessing logic
│   └── preprocessing.py
├── notebooks/            # EDA and visualization
│   └── 01-eda.ipynb
├── main.py               # Main pipeline script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


🚀 Getting Started
1. 📦 Prerequisites

Python 3.10 or higher
Virtual environment (recommended)

2. 🛠️ Setup
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd house-price-prediction-app

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

3. ▶️ Run the Application
python main.py

4. 🖱️ User Input Example
Enter house area (in sq.ft): 1600
Enter number of bedrooms: 3
Enter number of bathrooms: 2
Predicted Price: ₹315,000.00


📊 Outputs & Results

Predictions: Saved to outputs/predictions.csv
Visualizations:
Terminal-based plots using plotext
Optional image-based plots using matplotlib (saved to outputs/plot.png)


Model: Trained model saved to models/linear_model.pkl


✨ Features

✔️ Linear Regression model using Scikit-Learn
✔️ Interactive CLI for house price predictions
✔️ Terminal-based or image-based visualizations
✔️ Modular and well-organized code structure
✔️ Beginner-friendly with production-ready practices


📌 Sample Data Format (CSV)
Area,Bedrooms,Bathrooms,Price
1500,3,2,200000
1800,4,3,250000
...


