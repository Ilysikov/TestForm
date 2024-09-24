from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

import config
from fixtures import picture_, first_name, las_name, email_, gender_, mobile_, address_
import allure
from src.pages import IndexPage


class NewIndexPage(PageFactory, IndexPage):

    locators = {"firstname": ("ID", "firstName"),
                "lastname": ("ID", "lastName"),
                "email": ("ID", "userEmail"),
                "mobile": ("ID", "userNumber"),
                "picture": ("XPATH", "//input[@id='uploadPicture']"),
                "address": ("ID", "currentAddress")
                }
    @allure.step("Открываем страницу тестируемой формы")
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Remote(command_executor=config.container.command_executor,
                                       options=config.container.options)
        self.driver.implicitly_wait(8)
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.get(config.url.DOMAIN)

    @allure.step(f"Вводим рандомное слово в поле")
    def check_firstName(self, name):
        self.firstname.send_keys(name)

    @allure.step(f"Вводим рандомное слово в поле")
    def check_lastName(self, name):
        self.lastname.send_keys(name)

    @allure.step(f"Вводим рандомное слово в поле по одному символу")
    @allure.step(f"Кликаем по полю после ввода всех символов")
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
