import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # create object for browser control
    driver = webdriver.Chrome(
        service=Service(r'/Users/Alex Karmy/karmanovqaauto' + 'chromedriver.exe')
    )

    # open page https://github.com/login
    driver.get("https://github.com/login")

    # Search field for email input
    login_elem = driver.find_element(By.ID, "login_field")

    # input incorrect user name/login
    login_elem.send_keys("alexkarmincorrect@incorrectmail.com")

    # search field for password input
    pass_elem = driver.find_element(By.ID, "password")

    # input incorrect user password
    pass_elem.send_keys("incorrect password")

    # search sign in button
    btn_elem = driver.find_element(By.NAME, "commit")

    # emulating sign in click
    btn_elem.click()

    # check correct page name
    assert driver.title == "Sign in to GitHub · GitHub"

    # close browser
    driver.close()
