from fastapi import FastAPI
import assemblyai as aai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

app = FastAPI()

# AssemblyAI settings
aai.settings.api_key = api_key
transcriber = aai.Transcriber()
audio_url = "./disclaimer.mp3"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/assembly-ai")
async def assemblyEndpoint():
    transcript = transcriber.transcribe(audio_url)
    return transcript.text
