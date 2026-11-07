import pandas as pd
import streamlit as st

st.title("IoT Temperature Prediction Dashboard")
st.write("This project explores temperature and humidity sensor data.")

# Read the dataset
df = pd.read_csv("energydata_complete.csv")

# Keep only the columns we need
df = df[["date", "T1", "RH_1"]].copy()

# Use easier column names
df.columns = ["Time", "Temperature", "Humidity"]

# Clean the data
df["Time"] = pd.to_datetime(df["Time"], errors="coerce")

for column in ["Temperature", "Humidity"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna()
df = df.drop_duplicates(subset="Time")
df = df.sort_values("Time")

# Display a sample
st.subheader("Dataset Preview")
st.dataframe(df.head(10))

# Display basic information
st.subheader("Basic Statistics")
st.write("Number of readings:", len(df))
st.write("Average temperature (°C):", round(df["Temperature"].mean(), 2))
st.write("Average humidity (%):", round(df["Humidity"].mean(), 2))

# Let the user choose which sensor to display
sensor = st.selectbox(
    "Choose a sensor",
    ["Temperature", "Humidity"]
)

st.subheader(sensor + " Over Time")
st.line_chart(df.set_index("Time")[[sensor]])