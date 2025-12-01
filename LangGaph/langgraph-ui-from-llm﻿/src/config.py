import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

class Config:
    """Configuration management for the application."""
    
    # LLM Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # Default to gpt-4o or gpt-3.5-turbo if not specified
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")
    
    # Output Configuration
    # Resolve project root relative to this file (src/config.py -> project_root)
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")
    
    @classmethod
    def validate(cls):
        """Validate critical configuration."""
        if not cls.OPENAI_API_KEY:
            # Warning only, as user might want to swap client implementation
            print("WARNING: OPENAI_API_KEY not found in environment variables.")
