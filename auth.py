import streamlit as st
import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

# Read credentials from Streamlit secrets
creds_dict = st.secrets["gcp_service_account"]

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"])
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open("Mysamplecodes").sheet1

# Streamlit UI
st.title("Personnel Info App")

name = st.text_input("Enter name")
age = st.number_input("Enter age", min_value=0, step=1)

if st.button("Add Entry"):
    if name and age:
        sheet.append_row([name, int(age)])
        st.success(f"Added {name}, Age: {age}")
    else:
        st.error("Please enter both name and age.")
