
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.ai_gateway import ai_gateway

app = FastAPI(
    title="PROJECT YOUTUBE AI",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScriptRequest(BaseModel):
    topic: str = Field(min_length=3)
    language: str = "English"
    duration: int = Field(default=60, ge=15, le=180)


@app.get("/")
def home():
    return {
        "project": "PROJECT YOUTUBE AI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "backend": "online",
        "ai_connected": ai_gateway.is_connected()
    }


@app.get("/api/status")
def system_status():
    return {
        "research_ai": "pending",
        "script_ai": (
            "connected" if ai_gateway.is_connected()
            else "not_connected"
        ),
        "video_ai": "pending",
        "youtube_api": "pending"
    }


@app.post("/api/script")
def generate_script(request: ScriptRequest):

    prompt = f"""
Create a professional YouTube Shorts script.

Topic: {request.topic}
Language: {request.language}
Duration: {request.duration} seconds.

Requirements:
- Strong opening hook.
- Interesting factual storytelling.
- Clear and engaging narration.
- Strong ending.
- Do not invent historical facts.
- Separate narration and visual suggestions.
"""

    result = ai_gateway.generate(prompt)

    if not result["success"]:
        raise HTTPException(
            status_code=503,
            detail=result["error"]
        )

    return {
        "status": "success",
        "topic": request.topic,
        "script": result["content"]
    }

