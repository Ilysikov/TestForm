from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config
from fixtures import hobbies_, picture_, first_name, las_name, email_, gender_, mobile_, date_, subject_, states_, \
    address_


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)

    def open_index_page(self) -> None:
        self.driver.get(config.url.DOMAIN)

    def check_firstName(self):
        element = self.driver.find_element(By.ID, "firstName")
        element.send_keys(first_name["str"])

    def check_lastName(self):
        element = self.driver.find_element(By.ID, "lastName")
        element.send_keys(las_name["str"])

    def check_email(self):
        element = self.driver.find_element(By.ID, "userEmail")
        for u in email_["valid"]:
            element.send_keys(u)
        element.submit()

    def check_gender(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, gender_)))
        my_path = f'//div[@id="genterWrapper"]/div[2]/div[input[@id="{gender_}"]]'
        element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_path))
        element.click()

    def check_mobile(self):
        element = self.driver.find_element(By.ID, "userNumber")
        element.send_keys(mobile_["mobile"])

    def check_date(self):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "dateOfBirth"))
        element.click()
        element = self.wait.until(
            lambda wait: Select(wait.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select")))
        element.select_by_value(date_["valid_file"][-1])
        element = self.wait.until(
            lambda wait: Select(wait.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select")))
        element.select_by_value(date_["valid_file"][-2])
        day = ('00' + date_['valid_file'][0])[-3:]
        element = self.wait.until(lambda wait: wait.find_elements(By.CSS_SELECTOR,
                                                                  f"div[class^='react-datepicker__day react-datepicker__day--{day}'"))
        element = element[-1]
        element.click()

    def check_subject(self):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "subjectsInput"))
        for y in subject_["valid_subject"]:
            for t in y:
                element.send_keys(t)
            element.send_keys(keys.Keys.ENTER)

    def check_hobbies(self):
        for x in hobbies_:
            my_patch = f'//div[@id="hobbiesWrapper"]/div[2]/div[input[@id="{x}"]]'
            element = self.wait.until(lambda wait: wait.find_element(By.XPATH, my_patch))
            element.click()

    def check_picture(self):
        element = self.driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
        element.send_keys(f"{picture_['valid_file']}")

    def check_address(self):
        element = self.driver.find_element(By.ID, "currentAddress")
        element.send_keys(f"{address_['valid_address']}")

    def check_states(self):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "react-select-3-input"))
        for y in states_["valid_states"]:
            element.send_keys(y)
        element.send_keys(keys.Keys.RETURN)

    def check_city(self):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, "react-select-4-input"))
        for y in states_["valid_city"]:
            element.send_keys(y)
        element.send_keys(keys.Keys.RETURN)

    def check_submit(self):
        element = self.wait.until(lambda wait: wait.find_element(By.ID, f"currentAddress-label"))
        element.click()
        element = self.wait.until(lambda wait: wait.find_element(By.CSS_SELECTOR, f"button[class='btn btn-primary'"))
        element.click()
