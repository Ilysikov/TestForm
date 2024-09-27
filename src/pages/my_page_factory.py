import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
from seleniumpagefactory import PageFactory


class NewIndexPage(PageFactory):
    locators = {"firstname": ("ID", "firstName"),
                "lastname": ("ID", "lastName"),
                "email": ("ID", "userEmail"),
                "mobile": ("ID", "userNumber"),
                "picture": ("XPATH", "//input[@id='uploadPicture']"),
                "address": ("ID", "currentAddress"),
                "date_year": ("ID", "dateOfBirth"),
                "subject": ("ID", "subjectsInput"),
                "states": ("ID", "react-select-3-input"),
                "submit": ("ID", "currentAddress-label"),
                "city": ("ID", "react-select-4-input"),
                }

    def __init__(self, driver, wait):
        super().__init__()
        self.driver = driver
        self.wait = wait

    def check_gender(self, gender_):
        self.wait.until(EC.invisibility_of_element_located((By.ID, gender_)))
        my_path = f'//div[@id="genterWrapper"]/div[2]/div[input[@id="{gender_}"]]'
        element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_path))
        self.scrollbar(element)
        element.click()

    def check_date(self, date_):
        self.scrollbar(self.date_year)
        element = self.driver.find_element(By.ID, "dateOfBirth")
        element.click()
        element = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select"))
        element.select_by_value(date_[-1])
        element = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select"))
        element.select_by_value(date_[-2])
        day = ('00' + date_[0])[-3:]
        element = self.driver.find_elements(By.CSS_SELECTOR,
                                            f"div[class^='react-datepicker__day react-datepicker__day--{day}'")
        element = element[-1]
        element.click()
        self.mobile.click()

    def check_subject(self, subject_):
        element = self.wait.until(lambda d: d.find_element(By.ID, "subjectsInput"))
        for y in subject_:
            element.send_keys(y[0])
            time.sleep(1)
            self.wait.until(lambda d: d.find_element(By.XPATH, f'//div[contains(text(),"{y}")]')).click()
            time.sleep(1)

    def check_hobbies(self, hobbies_):
        for x in hobbies_:
            my_patch = f'//div[@id="hobbiesWrapper"]/div[2]/div[input[@id="{x}"]]'
            element = self.driver.find_element(By.XPATH, my_patch)
            webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()

    def check_states(self, states_):
        self.driver.find_element(By.XPATH, '//*[@id="state"]').click()
        self.wait.until(lambda d: d.find_element(By.XPATH, f'//div[contains(text(),"{states_}")]')).click()

    def check_city(self, city_):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="city"]'))).click()
        self.wait.until(lambda d: d.find_element(By.XPATH, f'//div[contains(text(),"{city_}")]')).click()

    def check_submit(self):
        webdriver.ActionChains(self.driver).move_to_element(self.submit).click(self.submit).perform()

    def scrollbar(self, element):
        scroll_origin = ScrollOrigin.from_element(element)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 200).perform()

    def check_firstName(self, name):
        self.firstname.send_keys(name)

    def check_lastName(self, name):
        self.lastname.send_keys(name)

    def check_email(self, email):
        for u in email:
            self.email.send_keys(u)
        self.email.submit()

    def check_mobile(self, mobile_):
        self.mobile.send_keys(mobile_)

    def check_picture(self, picture_):
        self.picture.send_keys(f"{picture_}")

    def check_address(self, address_):
        self.address.send_keys(f"{address_}")
