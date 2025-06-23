import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path):
    """
    Load the dataset from the specified path.
    """
    data = pd.read_csv(path)
    return data

def split_data(df, test_size=0.2, random_state=42):
    """
    Split the dataset into features (X) and target (y),
    then into training and testing sets.
    """
    X = df[["Area", "Bedrooms", "Bathrooms"]]
    y = df["Price"]\
    
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    """
    Scale the features using StandardScaler.
    """
    return X_train_scaled, X_test_scaled, scaler