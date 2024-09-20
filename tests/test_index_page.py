import allure
import pytest
from _pytest.hookspec import pytest_runtest_setup
from selenium.common import TimeoutException

from src import pages


class TestFooter:
    my_pages = [(pages.new_index_page)]

    @pytest.mark.parametrize("page", my_pages)
    @allure.title("Test input field firstname")
    def test_first(self, page, fix_name):
        page.check_firstName(fix_name[1])
        if not fix_name[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", my_pages)
    @allure.title("Test input field lastname")
    def test_last(self, page, fix_lastname):
        page.check_lastName(fix_lastname[1])
        if not fix_lastname[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", my_pages)
    @allure.title("Test input field email")
    def test_email(self, page, fix_email_):
        page.check_email(fix_email_[1])
        if not fix_email_[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", my_pages)
    @allure.title("Test input field gender")
    def test_gender(self, page, fix_gender_):
        page.check_gender(fix_gender_[1])
        if not fix_gender_[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", my_pages)
    def test_mobile(self, page, fix_mobile_):
        page.check_mobile(fix_mobile_)

    @pytest.mark.parametrize("page", my_pages)
    def test_date(self, page, fix_date_):
        page.check_date(fix_date_)

    @pytest.mark.parametrize("page", my_pages)
    def test_subjects(self, page, fix_subject_):
        page.check_subject(fix_subject_)

    @pytest.mark.parametrize("page", my_pages)
    def test_hobbies(self, page, fix_hobbies_):
        page.check_hobbies(fix_hobbies_)

    @pytest.mark.parametrize("page", my_pages)
    def test_picture(self, page, fix_picture_):
        page.check_picture(fix_picture_)

    @pytest.mark.parametrize("page", my_pages)
    def test_address(self, page, fix_address_):
        page.check_address(fix_address_)

    @pytest.mark.parametrize("page", my_pages)
    def test_states(self, page, fix_states_):
        page.check_states(fix_states_[1])
        if not fix_states_[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", my_pages)
    def test_city(self, page, fix_city_):
        page.check_city(fix_city_[1])
        if not fix_city_[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", my_pages)
    def test_submit(self, page):
        page.check_submit()
