from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import gspread
import pandas as pd
from io import StringIO
from pydantic import BaseModel

app = FastAPI()

class SheetURL(BaseModel):
    sheet_url: str

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        # Read CSV content
        contents = await file.read()

        # Attempt to decode the file with UTF-8, fallback to ISO-8859-1 if UTF-8 fails
        try:
            df = pd.read_csv(StringIO(contents.decode("utf-8")))
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(StringIO(contents.decode("ISO-8859-1")))
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Error decoding CSV file: {str(e)}")
        
        # Get columns and data
        columns = df.columns.tolist()
        data = df.to_dict(orient="records")
        
        return JSONResponse(content={"columns": columns, "data": data})
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing CSV: {str(e)}")

@app.post("/connect-sheet")
async def connect_sheet(sheet_url: SheetURL):
    try:
        # Authenticate and access the Google Sheet
        gc = gspread.service_account(filename='path-to-your-google-credentials.json')
        worksheet = gc.open_by_url(sheet_url.sheet_url).sheet1
        
        # Get data and columns from the sheet
        data = worksheet.get_all_records()
        columns = worksheet.row_values(1)  # Assuming first row is column headers
        
        return JSONResponse(content={"columns": columns, "data": data})
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error connecting to Google Sheet: {str(e)}")
