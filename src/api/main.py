from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Reseacrh Paper Recommender API is running"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    with open(f"uploaded_papers/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "File uploaded successfully"}