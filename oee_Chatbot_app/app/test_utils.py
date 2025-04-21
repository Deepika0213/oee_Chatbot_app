import pandas as pd
from utils import load_sensor_data, filter_data

def test_filter_data():
    # Load the Excel file
    file_path = "C:\\Users\\deepika.d\\Desktop\\oee_Chatbot_app\\oee_Chatbot_app\\app\\data\\sensor_data.xlsx"
    try:
        df = load_sensor_data(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return
    
    # Filter by machine ID, status, and month
    machine_id = "PKG_001"
    status = "Running"
    month = "2024-01"
    
    filtered = filter_data(df, machine_id=machine_id, status=status, month=month)
    
    # Print the filtered dataframe for testing purposes
    print(filtered)

# Run the test
test_filter_data()
