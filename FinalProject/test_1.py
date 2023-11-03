import time

import yaml

from FFinalProject.BaseApp import BasePage

from FinalProject.testpage2 import Operations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
passwd = testdata["password"]


def test_step(hello_user, browser, find_header, font_header):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login()
    page.enter_pass()
    page.click_login_button()
    assert page.get_hello_user() == hello_user
    page.click_about_button()
    time.sleep(3)
    assert page.header_find() == find_header
    time.sleep(3)
    assert page.header_font_size() == font_header