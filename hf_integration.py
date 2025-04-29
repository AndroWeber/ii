from huggingface_hub import HfApi

# Использование API-ключа для взаимодействия с Hugging Face
api = HfApi()

# Пример: получение списка моделей
models = api.list_models(token=HUGGINGFACE_API_KEY)
print("Доступные модели:", models)