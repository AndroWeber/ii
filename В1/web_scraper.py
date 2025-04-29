import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Пример: Извлечение всех блоков кода с сайта
        code_snippets = soup.find_all('code')
        return [code.get_text() for code in code_snippets]
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при доступе к {url}: {e}")
        return []

# Пример использования
if __name__ == "__main__":
    url = "https://www.selenium.dev/documentation/en/"
    data = scrape_website(url)
    for snippet in data[:5]:
        print(snippet)