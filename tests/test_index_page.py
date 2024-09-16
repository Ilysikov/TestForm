import allure
from src import pages
from utils.blok_try import trust


class TestFooter:


    pages.new_index_page.open_index_page()

    @allure.suite(suite_name="firstname")
    def test_first(self):
        pages.new_index_page.check_firstName()

    def test_last(self):
        pages.new_index_page.check_lastName()

    def test_email(self):
        pages.index_page.check_email()

    def test_gender(self):
        pages.index_page.check_gender()

    def test_mobile(self):
        pages.index_page.check_mobile()

    @trust
    def test_date(self):
        pages.index_page.check_date()

    def test_subjects(self):
        pages.index_page.check_subject()

    def test_hobbies(self):
        assert pages.index_page.check_hobbies() == True

    def test_picture(self):
        pages.index_page.check_picture()

    def test_address(self):
        pages.index_page.check_address()

    def test_states(self):
        pages.index_page.check_states()

    def test_city(self):
        pages.index_page.check_city()

    def test_submit(self):
        pages.index_page.check_submit()
