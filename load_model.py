from transformers import AutoModel, AutoTokenizer

# Использование API-ключа для загрузки модели
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=huggingface_api_key)
model = AutoModel.from_pretrained(model_name, use_auth_token=huggingface_api_key)

print("Модель успешно загружена!")