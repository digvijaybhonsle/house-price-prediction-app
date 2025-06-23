import os
import joblib
import logging
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from utils.preprocessing import load_data, split_data

# 📌 Logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    # 📁 Create folders
    os.makedirs("models", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    # 📥 Step 1: Load dataset
    df = load_data("data/housing.csv")

    # ✂️ Step 2: Split into train and test
    X_train, X_test, y_train, y_test = split_data(df)

    # 🤖 Step 3: Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 🔮 Step 4: Predict
    y_pred = model.predict(X_test)

    # 📊 Step 5: Evaluate
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    logging.info(f"R² Score: {r2:.4f}")
    logging.info(f"Mean Squared Error: {mse:.2f}")

    # 💾 Step 6: Save model
    joblib.dump(model, "models/linear_model.pkl")
    logging.info("✅ Model saved to models/linear_model.pkl")

    # 📤 Step 7: Save predictions to CSV
    predictions = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
    predictions.to_csv("outputs/predictions.csv", index=False)
    logging.info("📄 Predictions saved to outputs/predictions.csv")

    # 🔎 Step 8: Take user input & predict
    try:
        area = float(input("Enter house area (in sq.ft): "))
        bedrooms = int(input("Enter number of bedrooms: "))
        bathrooms = int(input("Enter number of bathrooms: "))

        new_input = [[area, bedrooms, bathrooms]]
        predicted_price = model.predict(new_input)

        logging.info(f"📌 Input: Area={area}, Bedrooms={bedrooms}, Bathrooms={bathrooms}")
        logging.info(f"💰 Predicted Price: ₹{predicted_price[0]:,.2f}")

    except ValueError:
        logging.error("❌ Invalid input. Please enter numeric values only.")
        return

    # 📈 Step 9: Plot Actual vs Predicted
    plt.figure(figsize=(8, 5))
    plt.scatter(y_test, y_pred, color='dodgerblue', edgecolors='k')
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted House Prices")
    plt.grid(True)
    plt.savefig("outputs/actual_vs_predicted.png")
    logging.info("📊 Plot saved to outputs/actual_vs_predicted.png")
    plt.show()
    logging.info("📊 Plot displayed successfully.")

# 🚀 Run main function
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"❌ Error: {e}")
