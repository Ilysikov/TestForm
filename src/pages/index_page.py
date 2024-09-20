import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory

import config
# from fixtures import hobbies_, picture_, first_name, las_name, email_, gender_, mobile_, date_, subject_, states_, \
#     address_
import allure
from utils import scrin


# from utils.blok_try import trust


class IndexPage:

    @allure.step("Открываем страницу тестируемой формы")
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(8)
        self.wait = WebDriverWait(driver, 20)
        self.driver.get(config.url.DOMAIN)

    @allure.step(f"Вводим рандомное слово в поле")
    @allure.step("Сохраняем себе скриншот страницы")
    def check_firstName(self, name):
        element = self.driver.find_element(By.ID, "firstName")
        element.send_keys(name)



    @allure.step(f"Кликаем по рандомно-избранному гендеру")
    def check_gender(self, gender_):
        self.wait.until(EC.invisibility_of_element_located((By.ID, gender_)))
        my_path = f'//div[@id="genterWrapper"]/div[2]/div[input[@id="{gender_}"]]'
        element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_path))
        element.click()


    def check_date(self, date_):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "dateOfBirth"))
        element.click()
        element = self.wait.until(
            lambda wait: Select(wait.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select")))
        element.select_by_value(date_[-1])
        element = self.wait.until(
            lambda wait: Select(wait.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select")))
        element.select_by_value(date_[-2])
        day = ('00' + date_[0])[-3:]
        element = self.wait.until(lambda wait: wait.find_elements(By.CSS_SELECTOR,
                                                                  f"div[class^='react-datepicker__day react-datepicker__day--{day}'"))
        element = element[-1]
        element.click()

    def check_subject(self, subject_):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "subjectsInput"))
        for y in subject_:
            for t in y:
                element.send_keys(t)
            element.send_keys(keys.Keys.ENTER)

    def check_hobbies(self, hobbies_):
        for x in hobbies_:
            print(hobbies_)
            my_patch = f'//div[@id="hobbiesWrapper"]/div[2]/div[input[@id="{x}"]]'
            element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_patch))
            element.click()



    def check_states(self, states_):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "react-select-3-input"))
        for y in states_:
            element.send_keys(y)
        element.send_keys(keys.Keys.RETURN)

    def check_city(self, states_):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "react-select-4-input"))
        for y in states_:
            element.send_keys(y)
        element.send_keys(keys.Keys.RETURN)

    def check_submit(self):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, f"currentAddress-label"))
        element.click()
        element = self.wait.until(lambda wait: wait.find_element(By.CSS_SELECTOR, f"button[class='btn btn-primary'"))
        element.click()

    def screenshot(self):
        name = f"/Users/ivanlysikov/PycharmProjects/TestForm/fixtures/photo/screnshot{random.randrange(100)}.png"
        self.driver.save_screenshot(name)
        return name

    def scrollbar(self):
        element = self.wait.until(lambda wait: wait.find_element(By.CSS_SELECTOR, f"button[class='btn btn-primary'"))
        ActionChains(self.driver).scroll_to_element(element).perform()


