
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com")
element = driver.find_element(By.ID, "example")
element.click()
driver.quit()
