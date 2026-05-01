from modules.processor import load_data, calculate_recovery_score
df = load_data()
df = calculate_recovery_score(df)
print(df[['date', 'Sleep_Hours', 'Heart_Rate_Bpm', 'Recovery_Score']].head(10))