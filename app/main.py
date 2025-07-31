import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from whisper_utils import transcribe_audio
from llm_utils import extract_meeting_data
from email_utils import generate_follow_up_email

app = FastAPI()

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    if file.content_type not in ["audio/mpeg", "audio/wav", "audio/x-wav", "audio/mp3"]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    
    # Save the uploaded file
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    try:
        transcript = transcribe_audio(file_location)
        decisions, action_items = extract_meeting_data(transcript)
        follow_up_email = generate_follow_up_email(transcript, decisions, action_items)
    finally:
        os.remove(file_location)

    return JSONResponse({
        "transcript": transcript,
        "decisions": decisions,
        "action_items": action_items,
        "follow_up_email": follow_up_email
    })
