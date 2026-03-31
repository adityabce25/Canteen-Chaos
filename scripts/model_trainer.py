import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

def train_canteen_model():
    # 1. Define Paths (Relative to the /scripts folder)
    # '..' means "go up one level" from /scripts to the project root
    data_path = os.path.join('..', 'data', 'canteen_data.csv')
    model_dir = os.path.join('..', 'models')
    
    # 2. Check if the /data folder and CSV exist
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found!")
        print("💡 Please run 'data_generator.py' first to create the dataset.")
        return

    # 3. Load Dataset (CO3: Data Representation)
    print("📂 Loading data from /data/canteen_data.csv...")
    df = pd.read_csv(data_path)

    # 4. Feature Engineering & Encoding (CO4)
    # Converting text categories (Day, Weather) into numerical values
    le_day = LabelEncoder()
    le_weather = LabelEncoder()
    
    df['Day_Enc'] = le_day.fit_transform(df['Day'])
    df['Weather_Enc'] = le_weather.fit_transform(df['Weather'])

    # 5. Define Features (X) and Target (y)
    # These are the inputs and the output for our Supervised Learning model
    X = df[['Day_Enc', 'Hour', 'Is_Exam_Week', 'Weather_Enc']]
    y = df['Wait_Time_Min']

    # 6. Train/Test Split (CO4: Validation Sets)
    # We use 80% to train the 'brain' and 20% to test its accuracy
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 7. Initialize and Train the Estimator (CO4: Machine Learning)
    print("🧠 Training the Random Forest model (this may take a second)...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 8. Evaluate Performance
    score = model.score(X_test, y_test)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    
    print("\n--- Training Results ---")
    print(f"✅ Accuracy (R2 Score): {score:.2f}")
    print(f"✅ Average Error: {mae:.2f} minutes")

    # 9. SAVE ASSETS (The Fix for FileNotFoundError)
    # This block ensures the /models directory exists before we try to save
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        print(f"📁 Created missing directory: {model_dir}")

    # Dumping the 'brain' files into the /models folder
    joblib.dump(model, os.path.join(model_dir, 'canteen_model.pkl'))
    joblib.dump(le_day, os.path.join(model_dir, 'le_day.pkl'))
    joblib.dump(le_weather, os.path.join(model_dir, 'le_weather.pkl'))
    
    print(f"💾 Success! Model and encoders saved in {model_dir}")

if __name__ == "__main__":
    train_canteen_model()