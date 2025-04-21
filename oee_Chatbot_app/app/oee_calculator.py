def calculate_oee(df, ideal_cycle_time=0.5):  # Ideal time in minutes/unit
    required_cols = ['Runtime (min)', 'Downtime (min)', 'Product_Count', 'Good_Products']
    if df.empty or not all(col in df.columns for col in required_cols):
        return None

    runtime = df['Runtime (min)'].sum()
    downtime = df['Downtime (min)'].sum()
    product_count = df['Product_Count'].sum()
    good_products = df['Good_Products'].sum()

    if runtime + downtime == 0 or runtime == 0 or product_count == 0:
        return None

    availability = runtime / (runtime + downtime)
    performance = (ideal_cycle_time * product_count) / runtime
    quality = good_products / product_count

    oee = availability * performance * quality * 100
    return round(min(oee, 100), 2)  # Cap at 100%

