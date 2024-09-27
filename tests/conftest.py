import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import config
from utils.random_data import RandomLastName, RandomEmail, RandomMobile, RandomPicture, \
    RandomDatetime, RandomSubjects, RandomStatesCity, RandomHobbies, RandomGender, RandomCurrentAddress, \
    RandomFirstName, RandomCity
from src.pages.my_page_factory import NewIndexPage


class My_data:
    @property
    def first_name(self):
        first_object = RandomFirstName()
        return first_object.my_dict()

    @property
    def las_name(self):
        las_object = RandomLastName()
        return las_object.my_dict()

    @property
    def email_(self):
        email_object = RandomEmail()
        return email_object.my_dict()

    @property
    def mobile_(self):
        mobile_object = RandomMobile()
        return mobile_object.my_dict()

    @property
    def picture_(self):
        picture_object = RandomPicture()
        return picture_object.my_dict()

    @property
    def address_(self):
        address_object = RandomCurrentAddress()
        return address_object.my_dict()

    @property
    def date_(self):
        date_object = RandomDatetime()
        return date_object.my_dict()

    @property
    def subject_(self):
        subject_object = RandomSubjects()
        return subject_object.my_dict()

    @property
    def states_(self):
        states_object = RandomStatesCity()
        return states_object.my_dict()

    @property
    def city_(self):
        city_object = RandomCity()
        return city_object.my_city(self.states_["valid_states"])

    @property
    def hobbies_(self):
        hobbies_object = RandomHobbies()
        return hobbies_object.my_dict()

    @property
    def gender_(self):
        gender_object = RandomGender()
        return gender_object.my_dict()


pro = My_data()


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(command_executor=config.container.command_executor,
                              options=config.container.options)
    driver.get(config.url.DOMAIN)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture(scope="class")
def wait(browser):
    return WebDriverWait(browser, 15)


@pytest.fixture
def page(request, browser, wait):
    dict_classes = {"new_index": NewIndexPage}
    page = dict_classes[request.param](browser, wait)
    return page


@pytest.fixture(params=[i for i in pro.first_name.keys()])
def fix_name(request):
    data = pro.first_name[request.param]
    excepted = request.param if request.param == "valid" else None
    return excepted, data


@pytest.fixture(params=[i for i in pro.las_name.keys()])
def fix_lastname(request):
    data = pro.las_name[request.param]
    excepted = request.param if request.param == "valid" else None
    return excepted, data


@pytest.fixture(params=[i for i in pro.email_.keys()])
def fix_email_(request):
    data = pro.email_[request.param]
    excepted = request.param if request.param == "valid" else None
    return excepted, data


@pytest.fixture(params=[i for i in pro.gender_.keys()])
def fix_gender_(request):
    data = pro.gender_[request.param]
    excepted = request.param if request.param == "valid" else None
    return excepted, data


@pytest.fixture(params=[pro.mobile_[i] if i == "valid" else pytest.param(pro.mobile_[i], marks=pytest.mark.xfail)
                        for i in pro.mobile_.keys()])
def fix_mobile_(request):
    return request.param


@pytest.fixture(params=[pro.hobbies_[i] if i == "valid" else pytest.param(pro.hobbies_[i], marks=pytest.mark.xfail)
                        for i in pro.hobbies_.keys()])
def fix_hobbies_(request):
    return request.param


@pytest.fixture(params=[pro.date_[i] if i == "valid" else pytest.param(pro.date_[i], marks=pytest.mark.xfail)
                        for i in pro.date_.keys()])
def fix_date_(request):
    return request.param


@pytest.fixture(params=[pro.subject_[i] if i == "valid" else pytest.param(pro.subject_[i], marks=pytest.mark.xfail)
                        for i in pro.subject_.keys()])
def fix_subject_(request):
    return request.param


@pytest.fixture(params=[pro.picture_[i] if i == "valid" else pytest.param(pro.picture_[i], marks=pytest.mark.xfail)
                        for i in pro.picture_.keys()])
def fix_picture_(request):
    return request.param


@pytest.fixture(params=[pro.address_[i] if i == "valid" else pytest.param(pro.address_[i], marks=pytest.mark.xfail)
                        for i in pro.address_.keys()])
def fix_address_(request):
    return request.param


@pytest.fixture(scope="session")
def fix_states_city():
    return pro.states_


@pytest.fixture(scope="session")
def fix_states_(fix_states_city):
    data = fix_states_city["valid_states"]
    return data


@pytest.fixture(scope="session")
def fix_city_(fix_states_city):
    data = fix_states_city["valid_city"]
    return data
