import os
import argparse
import requests
from flask import Flask, request, render_template
from src.main import AutonomousAI

# Создаем Flask-приложение
app = Flask(__name__)

# Глобальная переменная для системы ИИ
ai_system = None

# Встроенный API-ключ Hugging Face (НЕБЕЗОПАСНО, только для тестирования)
huggingface_api_key = "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"


@app.route('/')
def home():
    """
    Главная страница с окном для взаимодействия.
    """
    return render_template('index.html')


@app.route('/ai/interact', methods=['POST'])
def interact_with_ai():
    """
    REST API для взаимодействия с ИИ.
    """
    data = request.json
    user_input = data.get("user_input")
    target_ai = data.get("target_ai")

    if not user_input or not target_ai:
        return {"error": "Недостаточно данных"}, 400

    try:
        # Если выбрана Hugging Face нейросеть
        if target_ai == "huggingface":
            response = query_huggingface_model(user_input)
            return {"response": response}, 200

        # Иначе используем локальную систему ИИ
        output = ai_system.query_external_ai(target_ai, user_input)
        ai_system.store_data("queries", user_input)  # Сохранение запроса в базе данных
        return {"response": output}, 200
    except Exception as e:
        return {"error": str(e)}, 500


def query_huggingface_model(prompt):
    """
    Отправка запроса к модели Hugging Face.
    """
    if not huggingface_api_key:
        raise ValueError("API-ключ Hugging Face не указан!")
    
    headers = {
        "Authorization": f"Bearer {huggingface_api_key}"
    }
    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
    }

    # Пример использования модели GPT на Hugging Face
    url = "https://api-inference.huggingface.co/models/gpt2"

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise ValueError(f"Ошибка Hugging Face API: {response.status_code} - {response.text}")

    return response.json()


def main():
    """
    Основная точка входа в систему.
    """
    global ai_system

    parser = argparse.ArgumentParser(description="Запуск системы ИИ")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Хост для запуска API")
    parser.add_argument("--port", type=int, default=5000, help="Порт для запуска API")
    parser.add_argument("--database", type=str, default="ai_local.db", help="Путь к локальной базе данных")
    parser.add_argument("--external_ai_url", type=str, default=None, help="URL внешней нейросети для подключения")

    args = parser.parse_args()

    # Инициализация системы ИИ
    ai_system = AutonomousAI()

    # Подключение к локальной базе данных
    ai_system.connect_to_local_database(args.database)

    # Подключение к внешней нейросети, если URL указан
    if args.external_ai_url:
        print(f"Подключение к внешней нейросети по адресу {args.external_ai_url}...")
        ai_system.connect_to_external_ai(args.external_ai_url)
    else:
        print("Внешний URL не указан. Работаем в локальном режиме.")

    # Проверяем наличие API-ключа Hugging Face
    if huggingface_api_key:
        print("API-ключ Hugging Face успешно загружен.")
    else:
        print("API-ключ Hugging Face не указан. Функции Hugging Face будут недоступны.")

    # Запуск Flask API
    print(f"Запуск API на {args.host}:{args.port}...")
    app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()