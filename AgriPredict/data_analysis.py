import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generate_visuals():
    # 1. Setup folder
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    # 2. Load and Clean
    df = pd.read_csv('Rainfall.csv')
    df.columns = df.columns.str.strip()  # Clean hidden spaces in column names
    
    # Set a clean visual style
    sns.set_theme(style="whitegrid")
    
    # --- GRAPH 1: Rainfall Count (Simple Bar Chart) ---
    plt.figure(figsize=(8, 5))
    sns.countplot(x='rainfall', data=df, palette=['#ff9999','#66b3ff'])
    plt.title('Number of Rainy vs. Sunny Days', fontsize=14)
    plt.xlabel('Will it Rain?', fontsize=12)
    plt.ylabel('Number of Days', fontsize=12)
    plt.savefig('static/images/rainfall_count.png')
    plt.close()

    # --- GRAPH 2: Average Humidity for Rain (Easy to Understand) ---
    plt.figure(figsize=(8, 5))
    avg_hum = df.groupby('rainfall')['humidity'].mean().reset_index()
    sns.barplot(x='rainfall', y='humidity', data=avg_hum, palette='Greens_d')
    plt.title('Average Humidity: Rain vs No Rain', fontsize=14)
    plt.ylabel('Humidity Level (%)', fontsize=12)
    plt.savefig('static/images/humidity_avg.png')
    plt.close()

    # --- GRAPH 3: Temperature Trend (Simple Box Plot) ---
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='rainfall', y='temparature', data=df, palette='Oranges')
    plt.title('Temperature Range for Rainy Days', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.savefig('static/images/temp_range.png')
    plt.close()

    print("✅ Simple Visualizations Generated: Count, Humidity Avg, and Temp Range.")

if __name__ == "__main__":
    generate_visuals()