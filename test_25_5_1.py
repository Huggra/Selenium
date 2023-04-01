from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import numpy as np

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/DriverForGoogle/chromedriver.exe')
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

def tests_have_all_pets():
   pytest.driver.find_element(By.ID, 'email').send_keys('sda285696@mail.ru')
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pet1488Fr963')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
   pytest.driver.find_element(By.LINK_TEXT, u'Мои питомцы').click()

   names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:not(.smart_cell)')
   userStats = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>th>img')

   user_list = userStats.text.split()
   num_pets = int(user_list[2])
   user_photo = 0
   list_name_pets = []
   assert len(names) // 3 == num_pets  # Первый тест

def tests_have_half_photo():
   pytest.driver.find_element(By.ID, 'email').send_keys('sda285696@mail.ru')
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pet1488Fr963')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
   pytest.driver.find_element(By.LINK_TEXT, u'Мои питомцы').click()

   names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:not(.smart_cell)')
   userStats = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>th>img')

   user_list = userStats.text.split()
   num_pets = int(user_list[2])
   user_photo = 0
   list_name_pets = []

   for i in range(num_pets):
      if images[i].get_attribute('src') != '':
         user_photo += 1

   assert num_pets / 2 <= user_photo  # Второй тест

def tests_all_pets_have_name_type_age():
   pytest.driver.find_element(By.ID, 'email').send_keys('sda285696@mail.ru')
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pet1488Fr963')
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.implicitly_wait(5)
   pytest.driver.find_element(By.LINK_TEXT, u'Мои питомцы').click()

   names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:not(.smart_cell)')
   userStats = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>th>img')

   user_list = userStats.text.split()
   num_pets = int(user_list[2])
   user_photo = 0
   list_name_pets = []

   for i in range(len(names)):
      assert names[i].text != '' # Третий тест


def tests_all_pets_have_dif_names():
   pytest.driver.find_element(By.ID, 'email').send_keys('sda285696@mail.ru')
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pet1488Fr963')
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.implicitly_wait(5)
   pytest.driver.find_element(By.LINK_TEXT, u'Мои питомцы').click()

   names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:not(.smart_cell)')
   userStats = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>th>img')

   user_list = userStats.text.split()
   num_pets = int(user_list[2])
   user_photo = 0
   list_name_pets = []

   for i in range(len(names)):
      list_name_pets.append(names[i].text)
   list_name_pets_after = list_name_pets[0::3]
   list_name_pets_with_set = set(list_name_pets_after)

   assert len(list_name_pets_after) == len(list_name_pets_with_set)  # Четвертый тест

def tests_no_duplicate_pets():
   pytest.driver.find_element(By.ID, 'email').send_keys('sda285696@mail.ru')
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pet1488Fr963')
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.implicitly_wait(5)
   pytest.driver.find_element(By.LINK_TEXT, u'Мои питомцы').click()

   pytest.driver.implicitly_wait(5)
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:not(.smart_cell)')
   pytest.driver.implicitly_wait(5)
   userStats = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   pytest.driver.implicitly_wait(5)
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>th>img')

   user_list = userStats.text.split()
   num_pets = int(user_list[2])
   user_photo = 0
   list_name_pets = []

   for i in range(len(names)):
      list_name_pets.append(names[i].text)

   for i in range(len(list_name_pets)):
      for j in range(i + 1, len(list_name_pets)):
         if list_name_pets[i] in list_name_pets[j]:
            assert False # Пятый тест