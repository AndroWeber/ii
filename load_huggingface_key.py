from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API-ключа Hugging Face
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

# Пример использования ключа для взаимодействия с Hugging Face API
from huggingface_hub import HfApi

api = HfApi()
models = api.list_models(token=huggingface_api_key)
print(models)