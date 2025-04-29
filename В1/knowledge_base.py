# Простая база вопросов и ответов
knowledge_base = {
    "Как настроить Selenium?": "Установите библиотеку через pip: pip install selenium. Затем скачайте драйвер для вашего браузера.",
    "Как выполнить клик по элементу?": "Используйте метод click(): element.click()",
    "Как подождать загрузку элемента?": "Используйте WebDriverWait из selenium.webdriver.support.ui.",
    "Как работать с переносным жёстким диском?": "Используйте os и shutil для взаимодействия с файлами и папками."
}

def ask_question(question):
    return knowledge_base.get(question, "Извините, я не знаю ответа на этот вопрос.")

# Пример использования
if __name__ == "__main__":
    question = "Как выполнить клик по элементу?"
    answer = ask_question(question)
    print(f"Вопрос: {question}\nОтвет: {answer}")