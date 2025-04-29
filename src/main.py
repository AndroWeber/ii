import requests
import json
import sqlite3
import threading
from flask import Flask, request

# Flask для создания API
app = Flask(__name__)

class AutonomousAI:
    def __init__(self):
        self.db_connection = None
        self.external_apis = {
            "openai": "https://api.openai.com/v1/completions",
            "huggingface": "https://api-inference.huggingface.co/models"
        }
        self.api_keys = {
            "openai": "YOUR_OPENAI_API_KEY",
            "huggingface": "YOUR_HUGGINGFACE_API_KEY"
        }

    def connect_to_local_database(self, db_path):
        """
        Подключение к локальной базе данных.
        """
        try:
            self.db_connection = sqlite3.connect(db_path)
            print("Подключение к локальной базе данных выполнено успешно!")
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def query_external_ai(self, ai_name, input_text):
        """
        Отправка запроса к внешней AI-системе.
        """
        if ai_name not in self.external_apis:
            raise ValueError(f"API {ai_name} не поддерживается.")

        url = self.external_apis[ai_name]
        headers = {"Authorization": f"Bearer {self.api_keys[ai_name]}"}

        if ai_name == "openai":
            payload = {
                "model": "text-davinci-003",
                "prompt": input_text,
                "max_tokens": 50
            }
        elif ai_name == "huggingface":
            payload = {"inputs": input_text}

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка при запросе {ai_name}: {response.status_code}")
            return None

    def store_data(self, table, data):
        """
        Сохранение данных в локальную базу.
        """
        if not self.db_connection:
            raise ValueError("Нет подключения к базе данных.")
        cursor = self.db_connection.cursor()
        cursor.execute(f"INSERT INTO {table} (content) VALUES (?)", (data,))
        self.db_connection.commit()

    def train_model(self, data):
        """
        Логика самообучения модели на новых данных.
        """
        # Здесь можно использовать PyTorch или TensorFlow
        print("Обучение модели...")
        pass


@app.route('/ai/interact', methods=['POST'])
def interact_with_ai():
    """
    API для взаимодействия с ИИ.
    """
    data = request.json
    user_input = data.get("user_input")
    target_ai = data.get("target_ai")

    if not user_input or not target_ai:
        return {"error": "Недостаточно данных"}, 400

    try:
        output = ai_system.query_external_ai(target_ai, user_input)
        ai_system.store_data("queries", user_input)  # Сохраняем запрос в базе
        return {"response": output}, 200
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    # Создаем систему ИИ
    ai_system = AutonomousAI()

    # Подключаемся к локальной базе данных
    ai_system.connect_to_local_database("ai_local.db")

    # Запуск Flask API
    app.run(host="0.0.0.0", port=5000)