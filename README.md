# Earthquake_Data_Collection_Project

## Project Overview
This project collects real-time earthquake data from the USGS (United States Geological Survey) public API for the last 30 days. The data is saved in both CSV and GeoJSON formats for further analysis. A quick visualization scatter plot is also generated to show earthquake locations worldwide.

## Folder Structure

Earthquake\_Data\_Collection\_Project/
│
├── data/                                          # Collected CSV & JSON files
├── output/                                        # Generated plot images
|── collect_earthquakes.py                         # Script to fetch and save data
|── preview.py                                     # Script to visualize earthquake locations
├── requirements.txt                               # Python dependencies
├── README.md                                      # Project documentation


## Features
- Fetches last 30 days of earthquake data with magnitude ≥ 3.5
- Saves data in **CSV** and **JSON** formats
- Generates a scatter plot with bubble size proportional to magnitude
- Automatically creates required folders (`data/` and `output/`)

## Tools & Libraries
- Python 3
- Requests
- Pandas
- Matplotlib

## How to Run

1. **Set up a virtual environment** (optional but recommended)
# bash
python -m venv venv
source venv/bin/activate
# Windows
venv\Scripts\activate

3. **Install dependencies**

bash
pip install -r requirements.txt

3. **Run the data collection script**

bash
python collect_earthquakes.py

* This will create the CSV and JSON files in the `data/` folder.

4. **Run the visualization script**

bash
python preview_plot.py

* This will generate a scatter plot in the `output/` folder and display it.

## Output

* **Data**: `data/earthquakes_YYYY-MM-DD_to_YYYY-MM-DD.csv` and `.json`
* **Plot**: `output/earthquakes_plot.png`
