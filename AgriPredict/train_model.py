import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and clean
df = pd.read_csv('Rainfall.csv')
df.columns = df.columns.str.strip()

# Features based on your CSV: pressure, maxtemp, temparature, mintemp, humidity, windspeed
features = ['pressure', 'maxtemp', 'temparature', 'mintemp', 'humidity', 'windspeed']

# Convert target 'rainfall' (yes/no) to binary (1/0)
df['rainfall_binary'] = df['rainfall'].map({'yes': 1, 'no': 0}).fillna(0)

X = df[features].apply(pd.to_numeric, errors='coerce').fillna(0)
y = df['rainfall_binary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and accuracy
accuracy = model.score(X_test, y_test)
with open('model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'accuracy': accuracy}, f)

print(f"Model trained with {round(accuracy*100, 2)}% accuracy.")