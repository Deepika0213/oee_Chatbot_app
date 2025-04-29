#OEE Chatbot for Biscuit Packaging Devices

This Streamlit-based chatbot helps monitor and calculate the **Overall Equipment Effectiveness (OEE)** for biscuit packaging machines using sensor data from Excel sheets. It allows users to query a device's performance for a specific date and location.

---

## What is OEE?

**OEE (Overall Equipment Effectiveness)** is a standard for measuring manufacturing productivity. It shows how well a machine is utilized compared to its full potential.

---

## Features

- Load sensor data from Excel
- Filter data by:
  - Device ID
  - Date
  - Location (optional)
- Calculate:
  - **Availability**
  - **Performance**
  - **Quality**
  - Final **OEE (%)**
- User-friendly Streamlit interface

---

## OEE Calculation

OEE is calculated as:

OEE (%) = Availability × Performance × Quality × 100


###  Factor Definitions:
| Factor       | Formula                                 | Description                                  |
|--------------|------------------------------------------|----------------------------------------------|
| Availability | Runtime / (Runtime + Downtime)          | How often the machine was running            |
| Performance  | Actual Output / Ideal Output            | Was the machine running at ideal speed       |
| Quality      | Good Products / Total Products          | How many products were non-defective         |

---

##  Project Structure

oee_chatbot_app/ ├── app/ │ ├── chat_ui.py # Streamlit app │ ├── utils.py # Utility functions (data load + filter) │ ├── oee_calculator.py # OEE logic (availability, performance, quality) │ └── data/ │ └── sensor_data.xlsx ├── README.md └── requirements.txt



---

# Sample Sensor Data

| Device_ID | Date       | Runtime | Downtime | Product_Count | Good_Products | Location |
|-----------|------------|---------|----------|----------------|----------------|----------|
| PKG_001   | 01-01-2024 | 54      | 6        | 972            | 972            | Chennai  |

---


# Run the Streamlit app:

streamlit run app/chat_ui.py

