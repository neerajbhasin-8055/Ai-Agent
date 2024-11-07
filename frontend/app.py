import streamlit as st
import requests
import pandas as pd

# API URL for FastAPI backend
FASTAPI_URL = "http://localhost:8000"  # Update with your backend URL

# Title
st.title("File Upload and Google Sheets Connection")

# Sidebar for options
option = st.sidebar.selectbox("Select an Option", ["Upload CSV", "Connect to Google Sheets"])

# Handle CSV upload
if option == "Upload CSV":
    file = st.file_uploader("Browse CSV", type="csv")
    if file:
        try:
            # Call FastAPI endpoint to upload CSV
            files = {"file": file}
            response = requests.post(f"{FASTAPI_URL}/upload-csv", files=files)
            
            if response.status_code == 200:
                columns = response.json().get("columns")
                if columns:
                    column_name = st.selectbox("Select the main column", columns)
                    st.write(f"Selected Column: {column_name}")
                    data_preview = response.json().get("data", [])
                    if data_preview:
                        df = pd.DataFrame(data_preview)
                        st.write("Data Preview:", df.head())
            else:
                # Display error details from backend response
                st.error("Error uploading CSV file: " + response.json().get("detail", "Unknown error"))
        
        except requests.exceptions.RequestException as e:
            st.error(f"Error during CSV upload: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

# Handle Google Sheets connection
elif option == "Connect to Google Sheets":
    sheet_url = st.text_input("Enter Google Sheet URL")
    if sheet_url:
        try:
            # Call FastAPI endpoint to connect to Google Sheets
            response = requests.post(f"{FASTAPI_URL}/connect-sheet", json={"sheet_url": sheet_url})
            
            if response.status_code == 200:
                data = response.json().get("data")
                columns = response.json().get("columns")
                if data:
                    df = pd.DataFrame(data)
                    st.write("Data Preview:", df.head())
                    column_name = st.selectbox("Select the main column", columns)
                    st.write(f"Selected Column: {column_name}")
            else:
                # Display error details from backend response
                st.error("Error connecting to Google Sheet: " + response.json().get("detail", "Unknown error"))
        
        except requests.exceptions.RequestException as e:
            st.error(f"Error during Google Sheets connection: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
