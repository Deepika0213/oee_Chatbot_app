def calculate_oee(df):
    try:
        # Summing up relevant columns
        runtime = df['Runtime (min)'].sum()
        planned_time = df['Planned Time (min)'].sum()
        product_count = df['Product_Count'].sum()
        good_products = df['Good_Products'].sum()

        # Check if essential values are valid
        if runtime == 0 or planned_time == 0 or product_count == 0:
            return None

        # Heuristic: if Ideal_Cycle_Time is < 5, it's probably in seconds
        avg_ideal_cycle_time = df['Ideal_Cycle_Time'].mean()
        if avg_ideal_cycle_time < 5:
            ideal_cycle_time_min = avg_ideal_cycle_time / 60  # Convert seconds to minutes
        else:
            ideal_cycle_time_min = avg_ideal_cycle_time       # Already in minutes

        # Availability Calculation
        availability = runtime / planned_time

        # Performance Calculation (without capping at 100%)
        performance = (product_count * ideal_cycle_time_min) / runtime

        # Quality Calculation
        quality = good_products / product_count

        # OEE Calculation
        oee = availability * performance * quality * 100

        # Return the results (OEE capped at 100%)
        return {
            "oee": round(min(oee, 100), 2),
            "availability": round(min(availability * 100, 100), 2),
            "performance": round(min(performance * 100, 100), 2),
            "quality": round(min(quality * 100, 100), 2)
        }

    except Exception as e:
        return None
