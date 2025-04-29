import pandas as pd

def load_sensor_data(file_path):
    return pd.read_excel(file_path)

def filter_data(df, machine_id=None, date=None, location=None):
    # Required columns check
    required_columns = ['Device_ID', 'Date', 'Location', 'Planned_Time', 'Runtime',
                        'Ideal_Cycle_Time', 'Total_Count', 'Good_Count']
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns in Excel file: {missing_cols}")

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Ensure numeric columns are properly typed
    numeric_cols = ['Planned_Time', 'Runtime', 'Ideal_Cycle_Time', 'Total_Count', 'Good_Count']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Filter by device ID
    if machine_id:
        df = df[df['Device_ID'].str.upper() == machine_id.strip().upper()]

    # Filter by location
    if location:
        df = df[df['Location'].str.lower() == location.strip().lower()]

    # Filter by date
    if date:
        df = df[df['Date'].dt.date == date.date()]

    # Aggregate the data
    df_aggregated = df.groupby(['Device_ID', 'Date']).agg({
        'Planned_Time': 'sum',
        'Runtime': 'sum',
        'Ideal_Cycle_Time': 'mean',
        'Total_Count': 'sum',
        'Good_Count': 'sum'
    }).reset_index()

    # Rename columns for consistency with OEE calculation
    df_aggregated.rename(columns={
        'Planned_Time': 'Planned Time (min)',
        'Runtime': 'Runtime (min)',
        'Total_Count': 'Product_Count',
        'Good_Count': 'Good_Products'
    }, inplace=True)

    return df_aggregated


