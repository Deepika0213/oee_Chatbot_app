import pandas as pd

def load_sensor_data(file_path):
    return pd.read_excel(file_path)

def filter_data(df, machine_id=None, status=None, date=None, location=None):
    # Convert 'Date' column to datetime using known format
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')

    
    # Filter by machine ID
    if machine_id:
        df = df[df['Device_ID'] == machine_id]

    # Filter by status
    if status:
        df = df[df['Status'] == status]

    # Filter by location
    if location:
        df = df[df['Location'] == location]

    # Filter by specific date (ignoring time)
    if date:
        df = df[df['Date'].dt.date == date.date()]

    return df
