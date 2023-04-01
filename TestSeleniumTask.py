from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com')
search_input = selenium.find_element_by_name('q')
driver.quit()
