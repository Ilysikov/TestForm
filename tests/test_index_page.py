import allure
import pytest


class TestFooter:

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    @allure.title("Test input field firstname")
    @allure.step(f"Вводим рандомное слово в поле")
    def test_first(self, page, fix_name):
        page.check_firstName(fix_name[1])
        if not fix_name[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    @allure.title("Test input field lastname")
    @allure.step(f"Вводим рандомное слово в поле")
    def test_last(self, page, fix_lastname):
        page.check_lastName(fix_lastname[1])
        if not fix_lastname[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    @allure.title("Test input field email")
    @allure.step(f"Вводим рандомное слово в поле по одному символу")
    @allure.step(f"Кликаем по полю после ввода всех символов")
    def test_email(self, page, fix_email_):
        page.check_email(fix_email_[1])
        if not fix_email_[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    @allure.title("Test input field gender")
    @allure.step(f"Кликаем по рандомно-избранному гендеру")
    def test_gender(self, page, fix_gender_):
        page.check_gender(fix_gender_[1])
        if not fix_gender_[0]:
            pytest.xfail()

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_mobile(self, page, fix_mobile_):
        page.check_mobile(fix_mobile_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_date(self, page, fix_date_):
        page.check_date(fix_date_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_subjects(self, page, fix_subject_):
        page.check_subject(fix_subject_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_hobbies(self, page, fix_hobbies_):
        page.check_hobbies(fix_hobbies_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_picture(self, page, fix_picture_):
        page.check_picture(fix_picture_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_address(self, page, fix_address_):
        page.check_address(fix_address_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_states(self, page, fix_states_):
        page.check_states(fix_states_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_city(self, page, fix_city_):
        page.check_city(fix_city_)

    @pytest.mark.parametrize("page", ["new_index"], indirect=True)
    def test_submit(self, page):
        page.check_submit()
