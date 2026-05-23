from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://jsonplaceholder.typicode.com/posts"
MAX_TENTATIVAS = 3
ESPERA_INICIAL = 1