import os
import shutil
from pathlib import Path


def clean():
    path = Path("/Users/ivanlysikov/PycharmProjects/TestForm/tests/allure-results")
    for i in path.glob("**/*"):
        if i.name != "history":
            i.unlink()


def add_history():
    path2 = Path("/Users/ivanlysikov/PycharmProjects/TestForm/tests/allure-report/history")
    path3 = Path('/Users/ivanlysikov/PycharmProjects/TestForm/tests/allure-results/history')
    if not os.path.join('history'):
        os.mkdir(path3)
    for n in path2.glob("*"):
        shutil.copy(
            os.path.join(path2, n),
            os.path.join(path3))


if __name__ == "__main__":
    clean()
    os.system("pytest --alluredir allure-results")
    add_history()
    os.system("allure serve allure-results")
