import uvicorn
from fastapi import FastAPI, HTTPException
from utils.payloads import SubmissionPayload
from utils.file_utils import append_to_csv

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
    
if __name__ == "__main__":
    uvicorn.run("serve:app", host="0.0.0.0", port=8081, log_level="info")