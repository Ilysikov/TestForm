import base64
import json
import random
from pathlib import Path

import allure
import pytest
from fixtures.random_data import RandomLastName, RandomEmail, RandomMobile, RandomPicture, \
    RandomDatetime, RandomSubjects, RandomStatesCity, RandomHobbies, RandomGender, RandomCurrentAddress, RandomFirstName
from src import pages


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        web_driver = item.funcargs['page']

        name = web_driver.save_screenshot()
        actual = base64.b64encode(Path(name).read_bytes()).decode()
        content = json.dumps({"actual": f'data:image/png;base64,{actual}'}).encode()
        allure.attach(content,
                      name=f'screenshot[{str(random.randrange(1000))}]',
                      attachment_type='application/vnd.allure.image.diff')


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
    def hobbies_(self):
        hobbies_object = RandomHobbies()
        return hobbies_object.my_dict()

    @property
    def gender_(self):
        gender_object = RandomGender()
        return gender_object.my_dict()


pro = My_data()


@pytest.fixture
def page(request):
    dict_classes = {"new_index": pages.new_index_page}
    return dict_classes[request.param]


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


@pytest.fixture(params=[i for i in pro.states_.keys()])
def fix_states_(request):
    data = pro.states_[request.param]
    excepted = request.param if request.param == "valid_states" else None
    return excepted, data


@pytest.fixture(scope="session", params=[i for i in pro.states_.keys()])
def fix_city_(request):
    data = pro.states_[request.param]
    excepted = request.param if request.param == "valid_city" else None
    return excepted, data
