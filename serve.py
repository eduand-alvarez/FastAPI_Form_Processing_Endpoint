# main.py
from fastapi import FastAPI, HTTPException
from models import SubmissionPayload
from utils import append_to_csv

app = FastAPI()

@app.post("/submit/")
async def submit_model(payload: SubmissionPayload):
    try:
        # Convert payload to dictionary and append to CSV
        payload_dict = payload.dict()
        append_to_csv(payload_dict)
        
        return {"message": "Submission successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
