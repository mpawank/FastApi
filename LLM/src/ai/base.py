from abc import ABC, abstractmethod

class AIPlatform(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        """Sends a Prompt to the AI and returns the response text"""
        pass
