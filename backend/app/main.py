from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import random

app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/classify")
async def classify_image(image: UploadFile = File(...)):
    if image.content_type.split('/')[0] != 'image':
        raise HTTPException(status_code=400, detail="Invalid image file.")

    try:
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        
        # For demonstration purposes, we'll randomly classify images
        # In a real application, you would use a proper machine learning model
        is_approved = random.choice([True, False])
        
        return {"result": "Rizz Approved" if is_approved else "Not Rizz Approved"}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing image.") 