import pandas as pd
import numpy as np
import os

def generate_canteen_data():
    # 1. Setup Path (Saving to the /data folder)
    # We use os.path.join for compatibility between Windows/Mac/Linux
    output_path = os.path.join('..', 'data', 'canteen_data.csv')
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 2. Statistical Configuration (CO3)
    np.random.seed(42)  # Ensures the same data is generated every time
    n_samples = 1500    # Increased sample size for better ML training
    
    days = np.random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], n_samples)
    hours = np.random.randint(8, 18, n_samples)  # Operating hours: 8 AM to 5 PM
    is_exam_week = np.random.choice([0, 1], n_samples, p=[0.85, 0.15]) # 15% chance of exams
    weather = np.random.choice(['Sunny', 'Rainy', 'Cloudy'], n_samples, p=[0.6, 0.2, 0.2])

    # 3. Modeling Arrival Rates (CO3: Poisson Distribution)
    # Logic: More students arrive during lunch hours (12-1 PM)
    def get_arrival_rate(hour):
        if 12 <= hour <= 13: return 20  # Peak Lunch hour
        if 8 <= hour <= 10: return 10   # Breakfast rush
        return 6                        # Average off-peak
    
    # Generate random arrivals based on the hour's specific rate
    arrivals = [np.random.poisson(get_arrival_rate(h)) for h in hours]
    
    # 4. Calculating the Target Variable: Wait Time (CO3: Mean/Variance)
    wait_times = []
    for i in range(n_samples):
        # Base time is 5 minutes
        base = 5
        
        # Factors affecting wait (Syllabus: Deterministic vs Stochastic elements)
        hour_impact = 12 if 12 <= hours[i] <= 13 else 2
        weather_impact = 7 if weather[i] == 'Rainy' else 0 # Rainy = Crowded inside
        exam_impact = -4 if is_exam_week[i] == 1 else 0    # Exams = Library is full, Canteen empty
        
        # Add random "Noise" (CO3: Normal/Gaussian Distribution)
        # This represents random delays like a broken coffee machine or a slow cashier
        noise = np.random.normal(0, 2.5) 
        
        # Final formula (Wait Time depends on Arrivals + External Factors)
        total_wait = base + hour_impact + weather_impact + exam_impact + (arrivals[i] * 0.45) + noise
        
        # Ensure we don't have negative wait times
        wait_times.append(max(2.0, round(total_wait, 1)))

    # 5. Save to DataFrame (CO3: Data Representation)
    df = pd.DataFrame({
        'Day': days,
        'Hour': hours,
        'Is_Exam_Week': is_exam_week,
        'Weather': weather,
        'Arrivals': arrivals,
        'Wait_Time_Min': wait_times
    })
    
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Generated {n_samples} records.")
    print(f"📂 File saved at: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    generate_canteen_data()