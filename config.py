from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env
load_dotenv()

# Получение API-ключа Hugging Face
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")