from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.client import ClientHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.client = ClientHelper(self)


    def open_home_page(self):
        wd = self.wd
        if not ((wd.current_url.endswith("/addressbook")) and len(wd.find_elements_by_name("searchstring"))>0):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
