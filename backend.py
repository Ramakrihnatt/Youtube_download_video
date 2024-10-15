from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp

app = FastAPI()

# Enable CORS to allow cross-origin requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set the download directory to C:\Downloads (ensure this directory exists)
download_dir = "C:\\Downloads"

@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(download_dir, f"video-{link[-11:]}.mp4")  # Save to C:\Downloads
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download started"}
