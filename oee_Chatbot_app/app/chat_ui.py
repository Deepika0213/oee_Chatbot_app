import streamlit as st
from oee_calculator import calculate_oee
from utils import load_sensor_data, filter_data
import pandas as pd

# Page setup
st.set_page_config(page_title="OEE Chatbot", layout="centered")
st.title("🤖 OEE Chatbot for Biscuit Packaging Devices")
st.markdown("Ask me about a device's performance!")

# Inputs
device_id = st.text_input("🔍 Enter Device ID (e.g., PKG_001):")
date_input = st.text_input("🗓️ Enter Date (e.g., 2024-01-01):", "2024-01-01")
location = st.text_input("📍 Enter Location (optional):")

# Convert input date to datetime (expecting format: YYYY-MM-DD)
formatted_date = pd.to_datetime(date_input.strip(), format='%Y-%m-%d', errors='coerce')

if st.button("💬 Ask Bot"):
    try:
        # Load data
        df = load_sensor_data("C:\\Users\\deepika.d\\Desktop\\oee_Chatbot_app\\oee_Chatbot_app\\app\\data\\sensor_data.xlsx")

        # Ensure 'Date' column is in proper datetime format
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')

        # Optional: preview column names to confirm structure
        # st.write(df.columns)

        # Filter the data
        filtered = filter_data(df, machine_id=device_id, status="Running", date=formatted_date, location=location)

        # Display filtered results or warning
        if filtered.empty:
            st.warning("⚠️ No matching data found. Try a different Device ID or Date.")
        else:
            oee = calculate_oee(filtered)
            if oee is not None:
                st.success(f"✅ OEE for Device `{device_id}` during `{formatted_date.date()}` is: **{oee}%**")
                st.dataframe(filtered)
            else:
                st.warning("⚠️ OEE could not be calculated due to missing or invalid values.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
