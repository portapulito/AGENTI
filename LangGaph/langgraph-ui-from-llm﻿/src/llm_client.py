from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from .config import Config

class LLMClient:
    """Minimal wrapper for LLM interactions."""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=Config.MODEL_NAME,
            api_key=Config.OPENAI_API_KEY,
            temperature=0.7
        )

    def generate_html(self, system_prompt: str, user_prompt: str) -> str:
        """
        Generates HTML content based on system and user prompts.
        
        Args:
            system_prompt: The system instruction (persona/rules).
            user_prompt: The user's request.
            
        Returns:
            The generated text (HTML).
        """
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        return response.content
