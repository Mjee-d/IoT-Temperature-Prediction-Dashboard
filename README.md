# IoT Temperature Prediction Dashboard

This is a course project for IT351 – Data Science for the Internet of Things.

The aim is to explore temperature and humidity sensor data and build a dashboard that predicts future temperature readings.

## Current Progress

The first version of the dashboard is working. It displays sensor readings, basic statistics, and interactive charts.

The prediction model and model evaluation will be added next.

## Features

- Preview the first 10 sensor readings.
- Display the total number of readings.
- Display average temperature and humidity.
- Choose temperature or humidity using a dropdown.
- View how the selected sensor readings change over time.

## Dataset

This project uses the Appliances Energy Prediction dataset from the UCI Machine Learning Repository.

The selected columns are:

- `date`: Date and time of the reading.
- `T1`: Kitchen temperature in degrees Celsius.
- `RH_1`: Kitchen relative humidity in percent.

The readings are recorded at 10-minute intervals.

Dataset source:
https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction

Dataset credit:
Candanedo, L. (2017). Appliances Energy Prediction.
UCI Machine Learning Repository.
https://doi.org/10.24432/C5VC8G

The dataset is licensed under CC BY 4.0:
https://creativecommons.org/licenses/by/4.0/

The original CSV is included unchanged. The app selects and cleans the columns when it runs.

## Tools Used

- Python
- pandas
- Streamlit

## Data Preprocessing

The application:

1. Selects the time, temperature, and humidity columns.
2. Renames the columns to make them easier to understand.
3. Converts timestamps and sensor readings into suitable data types.
4. Removes rows with missing or invalid selected values.
5. Removes duplicate timestamps.
6. Sorts the readings by time.

## How to Run

Download this repository and extract it.

Open Anaconda Prompt and go to the extracted project folder.

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Start the dashboard:

```bash
python -m streamlit run app.py
```

Keep `energydata_complete.csv` in the same folder as `app.py`.


## Screenshots of the Dashboard

<img width="806" height="1374" alt="Screenshot 2026-11-07 183400" src="https://github.com/user-attachments/assets/be28b29a-3faa-4dac-bb86-022bf4004329" />
<img width="783" height="1347" alt="Screenshot 2026-11-07 183415" src="https://github.com/user-attachments/assets/da06be5a-d1c6-4329-8284-45b328fa1a3c" />
