# AI Agent for Data Retrieval from CSV/Google Sheets

## Project Overview
This project involves creating an AI agent that can read data from a CSV file or Google Sheets, perform web searches, and retrieve specific information about each entity in a chosen column. The agent leverages a language model (LLM) to parse web results based on user queries and formats the extracted data into a structured output. Users can upload their dataset, define search queries, and view/download the results.

## Features Completed So Far
### 1. **CSV File Upload**
   - Users can upload a CSV file containing entities (e.g., company names, products, etc.).
   - After uploading, the user is shown the available columns in the CSV and can select a main column (e.g., company names).

### 2. **Dynamic Query Input**
   - Users can input a custom query with placeholders (e.g., `What is the revenue of {company}?`).
   - The query is dynamically executed for each entity in the selected column, with placeholders replaced by actual entity names.

### 3. **Backend (FastAPI)**
   - A FastAPI backend handles file uploads, performs queries, and returns results.
   - The backend supports two main endpoints:
     - **/upload-csv**: Accepts CSV files, parses them, and returns the columns and data.
     - **/run-query**: Accepts the column name, query prompt, and data, and returns simulated query results for each entity.

### 4. **Frontend (Streamlit)**
   - A Streamlit frontend allows users to upload CSV files, select a column, and input queries.
   - It displays a preview of the uploaded data and the results after executing the query.

## Technologies Used
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Data Handling**: Pandas (for CSV parsing)
- **Web Requests**: Requests (for making API calls between frontend and backend)

## How to Use

### 1. **Clone the Project**
To get started with the project, first, clone the repository using Git. In your terminal, run:

```git clone https://github.com/your-username/your-repository-name.git```
### 2. **Set Up Virtual Environment (Recommended)**
It's best practice to use a virtual environment to manage the dependencies and keep your system environment clean.

Step-by-Step Guide:
Navigate to the Project Directory: Use the terminal or command prompt to go to the folder where you cloned the repository.


cd your-repository-name
Create a Virtual Environment: Run the following command to create a virtual environment named env:


python -m venv env
Activate the Virtual Environment:

On Windows:
.\env\Scripts\activate
On macOS/Linux:
source env/bin/activate
Install the Project Dependencies: Ensure your virtual environment is activated. Now, install all necessary project dependencies by running:

pip install -r requirements.txt
This will install all the libraries needed for both the backend and frontend (such as FastAPI, Streamlit, Pandas, and Requests).

### 3. **Running the Backend (FastAPI)**
Step-by-Step Guide:
Navigate to the Backend Folder: In your terminal, navigate to the folder where the backend code (e.g., main.py) is located.

Run the FastAPI Backend: To start the backend server, use Uvicorn:

uvicorn main:app --reload
The --reload flag allows automatic reloading of the server whenever you make changes to the code. The backend will be accessible at http://localhost:8000.

### 4. **Running the Frontend (Streamlit)**
Step-by-Step Guide:
Navigate to the Frontend Folder: Go to the folder where your frontend code (e.g., app.py) is located.

Run the Streamlit Frontend: Start the frontend by running:

streamlit run app.py
Access the Frontend: Streamlit will open a new tab in your default browser or you can manually go to http://localhost:8501 to interact with the app.

### 5. **Deactivating the Virtual Environment**
Once you are done working on the project, deactivate the virtual environment by running:

deactivate
Running Without a Virtual Environment (Not Recommended)
If you prefer not to use a virtual environment, you can install the required dependencies globally. Run the following command to install the dependencies:

pip install fastapi uvicorn pandas streamlit requests
Then, follow the same steps to run the backend and frontend as mentioned above.

### Key Points:
- **Set up of virtual environment**: Provides clear instructions on setting up a virtual environment and installing dependencies.
- **Alternative to virtual environment**: Offers instructions for users who prefer installing dependencies globally.
- **Backend and Frontend Setup**: Provides the necessary steps to run both the backend (FastAPI) and frontend (Streamlit).
- **Deactivating the environment**: Includes a section on deactivating the virtual environment after use.

This should make it easy for anyone to clone the project, set it up, and start contributing!
