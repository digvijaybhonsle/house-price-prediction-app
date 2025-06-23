import argparse
import joblib

def predict_price(area, bedrooms, bathrooms):
    model = joblib.load("models/linear_model.pkl")
    input_data = [[area, bedrooms, bathrooms]]
    prediction = model.predict(input_data)
    print(f"Predicted price for {area} sqft, {bedrooms}BHK, {bathrooms} bath: ₹{prediction[0]:,.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--area", type=int, required=True)
    parser.add_argument("--bedrooms", type=int, required=True)
    parser.add_argument("--bathrooms", type=int, required=True)
    args = parser.parse_args()

    predict_price(args.area, args.bedrooms, args.bathrooms)