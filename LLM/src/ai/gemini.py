
import os
from .base import AIPlatform
import google.generativeai as google


class Gemini(AIPlatform):
    def __init__(self, api_key, system_prompt: str = None):
        self.api_key = api_key
        self.system_prompt = system_prompt
        google.configure(api_key=self.api_key)
        self.model = google.GenerativeModel("gemini-2.5-flash-preview-05-20")

    def chat(self, prompt: str) -> str:
        if self.system_prompt:
            prompt = f"{self.system_prompt}\n\n{prompt}"
        response = self.model.generate_content(prompt)
        return response.text


def load_system_prompt():
    with open("src/prompts/system_prompt.md", "r") as file:
        return file.read()
