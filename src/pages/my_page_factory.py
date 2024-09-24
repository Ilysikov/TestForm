import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from seleniumpagefactory import PageFactory

import config


class NewIndexPage(PageFactory):
    locators = {"firstname": ("ID", "firstName"),
                "lastname": ("ID", "lastName"),
                "email": ("ID", "userEmail"),
                "mobile": ("ID", "userNumber"),
                "picture": ("XPATH", "//input[@id='uploadPicture']"),
                "address": ("ID", "currentAddress")
                }

    def __init__(self):
        super().__init__()
        self.driver = webdriver.Remote(command_executor=config.container.command_executor,
                                       options=config.container.options)
        self.driver.implicitly_wait(8)
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.get(config.url.DOMAIN)

    def check_gender(self, gender_):
        self.wait.until(EC.invisibility_of_element_located((By.ID, gender_)))
        my_path = f'//div[@id="genterWrapper"]/div[2]/div[input[@id="{gender_}"]]'
        by, loc = By.XPATH, my_path
        self.scrollbar(by, loc)
        element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_path))
        element.click()

    def check_date(self, date_):
        by, loc = By.ID, "dateOfBirth"
        self.scrollbar(by, loc)
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
        by, loc = By.ID, "subjectsInput"
        self.scrollbar(by, loc)
        for y in subject_:
            for t in y:
                element.send_keys(t)
            element.send_keys(keys.Keys.ENTER)
            self.scrollbar(by, "react-select-4-input")
            self.scrollbar(by, loc)

    def check_hobbies(self, hobbies_):
        for x in hobbies_:
            my_patch = f'//div[@id="hobbiesWrapper"]/div[2]/div[input[@id="{x}"]]'
            element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_patch))
            element.click()

    def check_states(self, states_):
        by, loc = By.ID, "react-select-3-input"
        self.scrollbar(by, loc)
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
        by, loc = By.CSS_SELECTOR, f"button[class='btn btn-primary'"
        self.scrollbar(by, loc)
        element = self.wait.until(lambda wait: wait.find_element(By.ID, f"currentAddress-label"))
        element.click()
        element = self.wait.until(lambda wait: wait.find_element(by, loc))
        element.click()

    def screenshot(self):
        name = f"/Users/ivanlysikov/PycharmProjects/TestForm/fixtures/photo/screnshot{random.randrange(100)}.png"
        self.driver.save_screenshot(name)
        return name

    def scrollbar(self, by, loc):
        element = self.wait.until(lambda wait: wait.find_element(by, loc))
        ActionChains(self.driver).scroll_to_element(element).perform()

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
