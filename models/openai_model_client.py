from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
from config.constants import MODEL_OPENAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(model=MODEL_OPENAI)
    return openai_model_client
