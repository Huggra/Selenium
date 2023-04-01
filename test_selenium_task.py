from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import time


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/DriverForGoogle/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('sda285696@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pet1488Fr963')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   print(images)

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ' '
      assert names[i].text != ' '
      assert descriptions[i].text != ' '
      assert ', ' in descriptions[i].text
      print(images[i].get_attribute('src'))
      # parts = descriptions[i].text.split(", ")
      # assert len(parts[0]) > 0
      # assert len(parts[1]) > 0
