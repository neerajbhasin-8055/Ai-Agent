from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import pandas as pd
from io import StringIO

app = FastAPI()

# Pydantic model to validate query input
class QueryRequest(BaseModel):
    column_name: str
    prompt: str
    data: List[dict]

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        # Read CSV content
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        # Get columns and data
        columns = df.columns.tolist()
        data = df.to_dict(orient="records")

        return JSONResponse(content={"columns": columns, "data": data})

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing CSV: {str(e)}")

@app.post("/run-query")
async def run_query(request: QueryRequest):
    results = []

    try:
        column_name = request.column_name
        prompt = request.prompt
        data = request.data

        # Process each row in the data
        for row in data:
            entity = row.get(column_name)
            if not entity:
                continue  # Skip rows without the entity value

            query = prompt.replace("{entity}", str(entity))
            
            # Simulate the result (you can replace this with actual querying logic)
            response_data = {"entity": entity, "query_result": f"Simulated result for '{query}'"}
            results.append(response_data)

        return JSONResponse(content={"results": results})

    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Error processing query: {str(e)}")
