import streamlit as st
from oee_calculator import calculate_oee
from utils import load_sensor_data
import pandas as pd

# Page setup
st.set_page_config(page_title="OEE Chatbot", layout="centered")
st.title("🤖 OEE Chatbot for Biscuit Packaging Devices")
st.markdown("Ask me about a device's performance!")

# Inputs
device_id = st.text_input("🔍 Enter Device ID (e.g., PCKG_001):")
date_input = st.text_input("🗓️ Enter Date (e.g., 2024-01-01):", "2024-01-01")
location = st.text_input("📍 Enter Location (optional):")

# Convert input date to datetime
formatted_date = pd.to_datetime(date_input.strip(), format='%Y-%m-%d', errors='coerce')

# Handle case for invalid date input
if pd.isna(formatted_date):
    st.warning("⚠️ The date format is invalid. Please use the format 'YYYY-MM-DD'.")
else:
    if st.button("💬 Ask Bot"):
        try:
            # Load the sensor data
            df = load_sensor_data("C:\\Users\\deepika.d\\Desktop\\oee_Chatbot_app\\oee_Chatbot_app\\app\\data\\iot_sensor_data_daily.xlsx")

            # Convert 'Date' column to datetime
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Filter the data based on inputs
            filtered = df[
                (df['Device_ID'].str.upper() == device_id.strip().upper()) &
                (df['Date'].dt.date == formatted_date.date())
            ]

            if location:
                filtered = filtered[filtered['Location'].str.lower() == location.lower()]

            if filtered.empty:
                st.warning("⚠️ No matching data found. Try a different Device ID or Date.")
            else:
                # Rename columns to expected names
                filtered = filtered.rename(columns={
                    'Runtime': 'Runtime (min)',
                    'Planned_Time': 'Planned Time (min)',
                    'Total_Count': 'Product_Count',
                    'Good_Count': 'Good_Products'
                })

                # Check if Ideal_Cycle_Time exists and is valid
                if 'Ideal_Cycle_Time' not in filtered.columns or filtered['Ideal_Cycle_Time'].isnull().all():
                    st.warning("⚠️ Ideal Cycle Time is missing or invalid.")
                else:
                    # Calculate OEE
                    # Calculate OEE directly from DataFrame
                    oee_result = calculate_oee(filtered)

                    

                    if oee_result:
                        st.success(f"✅ OEE for Device `{device_id}` during `{formatted_date.date()}` is: **{oee_result['oee']}%**")
                        st.markdown(f"""
                        ### 📊 OEE Breakdown
                        - **Availability:** {oee_result['availability']}%
                        - **Performance:** {oee_result['performance']}%
                        - **Quality:** {oee_result['quality']}%
                        """)
                        st.dataframe(filtered)
                    else:
                        st.warning("⚠️ OEE could not be calculated due to missing or invalid values.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
