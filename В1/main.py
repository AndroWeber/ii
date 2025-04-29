import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget, QFileDialog
from transformers import AutoModelForCausalLM, AutoTokenizer
from website_analyzer import analyze_website
from test_plan_generator import generate_test_plan

class AIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Локальный ИИ Ассистент")
        self.setGeometry(100, 100, 800, 600)

        # Инициализация интерфейса
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.input_field = QTextEdit(self)
        self.input_field.setPlaceholderText("Введите ваш запрос или URL для анализа...")
        self.layout.addWidget(self.input_field)

        self.response_field = QTextEdit(self)
        self.response_field.setReadOnly(True)
        self.layout.addWidget(self.response_field)

        self.analyze_button = QPushButton("Анализировать сайт", self)
        self.analyze_button.clicked.connect(self.analyze_site)
        self.layout.addWidget(self.analyze_button)

        self.test_plan_button = QPushButton("Создать тест-план", self)
        self.test_plan_button.clicked.connect(self.create_test_plan)
        self.layout.addWidget(self.test_plan_button)

        self.send_button = QPushButton("Ответить на запрос", self)
        self.send_button.clicked.connect(self.handle_request)
        self.layout.addWidget(self.send_button)

        # Загрузка модели ИИ
        self.model_path = "./model"  # Путь к локальной модели
        if os.path.exists(self.model_path):
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_path)
        else:
            self.response_field.setPlainText("Модель не найдена! Проверьте правильность пути к модели.")

    def handle_request(self):
        user_input = self.input_field.toPlainText()
        if user_input.strip():
            try:
                inputs = self.tokenizer(user_input, return_tensors="pt")
                outputs = self.model.generate(**inputs, max_length=200)
                response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
                self.response_field.setPlainText(response)
            except Exception as e:
                self.response_field.setPlainText(f"Ошибка обработки запроса: {e}")
        else:
            self.response_field.setPlainText("Введите запрос для ИИ.")

    def analyze_site(self):
        url = self.input_field.toPlainText().strip()
        if url:
            try:
                report = analyze_website(url)
                self.response_field.setPlainText(report)
            except Exception as e:
                self.response_field.setPlainText(f"Ошибка анализа сайта: {e}")
        else:
            self.response_field.setPlainText("Введите URL сайта для анализа.")

    def create_test_plan(self):
        description = self.input_field.toPlainText().strip()
        if description:
            try:
                test_plan = generate_test_plan(description)
                self.response_field.setPlainText(test_plan)
            except Exception as e:
                self.response_field.setPlainText(f"Ошибка создания тест-плана: {e}")
        else:
            self.response_field.setPlainText("Введите описание задачи для генерации тест-плана.")

# Главная функция
def main():
    app = QApplication(sys.argv)
    window = AIApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()