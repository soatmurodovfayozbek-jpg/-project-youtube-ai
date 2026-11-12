
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="PROJECT YOUTUBE AI",
    description="AI-powered YouTube automation system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScriptRequest(BaseModel):
    topic: str
    language: str = "English"
    duration: int = 60

@app.get("/")
def home():
    return {
        "project": "PROJECT YOUTUBE AI",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "online"
    }

@app.get("/api/status")
def system_status():
    return {
        "research_ai": "not_connected",
        "script_ai": "not_connected",
        "video_ai": "not_connected",
        "youtube_api": "not_connected"
    }

@app.post("/api/script")
def generate_script(request: ScriptRequest):
    if not request.topic.strip():
        return {"error": "Topic is required"}

    return {
        "status": "waiting_for_ai",
        "topic": request.topic,
        "language": request.language,
        "duration": request.duration,
        "message": "AI provider must be connected."
    }
