import subprocess

def execute_generated_code(code):
    # Сохраняем код в файл
    try:
        with open("generated_test.py", "w") as file:
            file.write(code)
        
        # Выполняем код
        result = subprocess.run(["python", "generated_test.py"], capture_output=True, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", f"Ошибка выполнения кода: {e}"

# Пример использования
if __name__ == "__main__":
    code = """
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com")
element = driver.find_element(By.ID, "example")
element.click()
driver.quit()
"""
    stdout, stderr = execute_generated_code(code)
    print("Вывод программы:", stdout)
    print("Ошибки:", stderr)