from dotenv import load_dotenv

import os

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

NEO4J_URI = os.getenv("NEO4J_URI")

NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")

NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

FASTAPI_HOST = os.getenv("FASTAPI_HOST")

FASTAPI_PORT = os.getenv("FASTAPI_PORT")