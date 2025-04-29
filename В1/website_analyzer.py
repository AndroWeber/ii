from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def analyze_website(url):
    report = []
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        # Проверка доступности элементов
        links = driver.find_elements(By.TAG_NAME, "a")
        broken_links = []
        for link in links:
            try:
                href = link.get_attribute("href")
                if href and "http" in href:
                    driver.get(href)
                    if driver.title == "404":
                        broken_links.append(href)
            except:
                broken_links.append(href)

        # Отчёт
        report.append(f"Обнаружено ссылок: {len(links)}")
        report.append(f"Сломанных ссылок: {len(broken_links)}")
        report.append("\nСписок сломанных ссылок:")
        report.extend(broken_links)

        # Проверка времени загрузки страницы
        start_time = time.time()
        driver.refresh()
        load_time = time.time() - start_time
        report.append(f"\nВремя загрузки страницы: {load_time:.2f} секунд")

        driver.quit()
    except Exception as e:
        report.append(f"Ошибка анализа: {e}")
    return "\n".join(report)