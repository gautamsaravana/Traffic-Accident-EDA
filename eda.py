import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Load dataset
# -----------------------------
df = pd.read_csv("US_Accidents_March23.csv")

# -----------------------------
# Step 2: Basic Info
# -----------------------------
print("First 10 rows:")
print(df.head(10))

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Step 3: Data Cleaning
# -----------------------------

# Handle datetime error (IMPORTANT FIX)
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')

# Remove invalid datetime rows
df = df.dropna(subset=['Start_Time'])

# Fill missing categorical values
if 'Weather_Condition' in df.columns:
    df['Weather_Condition'] = df['Weather_Condition'].fillna(df['Weather_Condition'].mode()[0])

# -----------------------------
# Step 4: Feature Engineering
# -----------------------------

# Extract hour
df['Hour'] = df['Start_Time'].dt.hour

# -----------------------------
# Step 5: Analysis
# -----------------------------

# Accidents by Weather
if 'Weather_Condition' in df.columns:
    weather_counts = df['Weather_Condition'].value_counts().head(10)
    print("\nTop Weather Conditions:\n", weather_counts)

# Accidents by Hour
hour_counts = df['Hour'].value_counts().sort_index()
print("\nAccidents by Hour:\n", hour_counts)

# -----------------------------
# Step 6: Visualization
# -----------------------------

# Weather Plot
if 'Weather_Condition' in df.columns:
    plt.figure()
    weather_counts.plot(kind='bar')
    plt.title("Top 10 Weather Conditions for Accidents")
    plt.xlabel("Weather")
    plt.ylabel("Number of Accidents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("weather_plot.png")
    plt.show()

# Time Plot
plt.figure()
hour_counts.plot(kind='line')
plt.title("Accidents by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("time_plot.png")
plt.show()

# -----------------------------
# Step 7: Final Insights
# -----------------------------
print("\nPeak Accident Hours:")
print(hour_counts.sort_values(ascending=False).head())