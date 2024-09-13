import pages
import pytest
import allure

class TestFooter:
    pages.index_page.open_index_page()


    @allure.suite(suite_name="firstname")
    def test_first(self):
        pages.index_page.check_firstName()
    @pytest.mark.skip(reason="check")
    def test_last(self):
        pages.index_page.check_lastName()

    def test_email(self):
        pages.index_page.check_email()

    def test_gender(self):
        pages.index_page.check_gender()

    def test_mobile(self):
        pages.index_page.check_mobile()

    def test_date(self):
        pages.index_page.check_date()

    def test_subjects(self):
        pages.index_page.check_subject()

    def test_hobbies(self):
        pages.index_page.check_hobbies()

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
