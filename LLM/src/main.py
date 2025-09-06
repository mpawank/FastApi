import os
from fastapi import FastAPI
from pydantic import BaseModel
from .ai.gemini import Gemini, load_system_prompt

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post('/chat', response_model=ChatResponse)
async def chat(request: ChatRequest):

    response_text = "..."
    return ChatResponse(response=response_text)

system_prompt = load_system_prompt()
gemini_api_key = os.getenv("GOOGLE_API_KEY")

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)
