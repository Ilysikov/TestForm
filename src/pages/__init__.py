from src.pages.index_page import IndexPage
from src.pages.my_page_factory import NewIndexPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixtures import picture_, first_name, las_name, email_, gender_, mobile_, address_
import allure

# index_pag = IndexPage(webdriver.Chrome())
new_index_page = NewIndexPage()
