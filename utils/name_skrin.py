from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config
from fixtures import hobbies_, picture_, first_name, las_name, email_, gender_, mobile_, date_, subject_, states_, \
    address_
import allure
import os


class NamePhoto:
    directory = "/Users/ivanlysikov/PycharmProjects/TestForm/fixtures/photo"
    format="png"

    name_file = os.listdir(directory)

    def new_file(self, element):
        self.new_file=f"{self.directory}{first_name['str'] + str(element)}.{self.format}"
        count=0
        while self.new_file in self.name_file:
            count+=1
            self.new_file=f"/{self.directory}{first_name['str'] + str(element)}{str(count)}.{self.format}"
        return self.new_file