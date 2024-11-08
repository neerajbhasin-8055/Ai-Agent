import streamlit as st
import requests
import pandas as pd

# API URL for FastAPI backend
FASTAPI_URL = "http://localhost:8000"  # Update with your backend URL if needed

# Title
st.title("File Upload and Query")

# Handle CSV upload
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
                    st.write("Data Preview:", df)

                    # Prompt input for dynamic query
                    st.write("Specify the information you want to retrieve:")
                    prompt = st.text_input("Enter your custom prompt (use {entity} as a placeholder)")

                    # Run Query button
                    if st.button("Run Query"):
                        if prompt:  # Ensure the prompt is not empty
                            query_payload = {
                                "column_name": column_name,
                                "prompt": prompt,
                                "data": data_preview
                            }
                            # Make sure the payload is in JSON format
                            query_response = requests.post(f"{FASTAPI_URL}/run-query", json=query_payload)

                            if query_response.status_code == 200:
                                st.write("Query Results:")
                                query_results = query_response.json().get("results")
                                st.write(pd.DataFrame(query_results))
                            else:
                                st.error("Error running query: " + query_response.json().get("detail", "Unknown error"))
                        else:
                            st.error("Please enter a query prompt.")
        else:
            st.error("Error uploading CSV file.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
