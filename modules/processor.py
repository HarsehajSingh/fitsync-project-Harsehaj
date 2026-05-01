import pandas as pd

def process_data():
    data = load_data()
    return calculate_recovery_score(data)

def load_data():
    file_path = 'data/health_data.csv'
    data = pd.read_csv(file_path)

    # Convert date
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Fill missing values
    data['Steps'].fillna(data['Steps'].median(), inplace=True)
    data['Sleep_Hours'].fillna(7.0, inplace=True)
    data['Heart_Rate_bpm'].fillna(68, inplace=True)

    numeric_cols = data.select_dtypes(include='number').columns
    for col in numeric_cols:
        data[col].fillna(data[col].median(), inplace=True)

    return data

def calculate_recovery_score(df):
    scores = []

    for _, row in df.iterrows():
        score = 50

        # Sleep
        if row['Sleep_Hours'] >= 7:
            score += 20
        elif row['Sleep_Hours'] < 6:
            score -= 20

        # Heart rate
        if 50 <= row['Heart_Rate_bpm'] <= 95:
            if row['Heart_Rate_bpm'] < 60:
                score += 10
            elif row['Heart_Rate_bpm'] > 80:
                score -= 10

        # Steps
        if 4000 <= row['Steps'] <= 16000:
            if row['Steps'] < 10000:
                score += 10
            else:
                score -= 5

        score = max(0, min(100, score))
        scores.append(score)

    df['Recovery_Score'] = scores
    return df