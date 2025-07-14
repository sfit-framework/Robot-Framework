from time import sleep

from SeleniumLibrary import SeleniumLibrary
from Variables.config import Config
from locators.HomeLocators import HomeLocators


class HomeKeywords:
    def __init__(self):
        self.selenium = SeleniumLibrary()


    def open_amazon_homepage(self):
        self.selenium.open_browser(Config.AMAZON_URL, "chrome")
        self.selenium.maximize_browser_window()

    def search_for_product(self, product_name):
        self.selenium.input_text(HomeLocators.SEARCH_BAR, product_name)
        self.selenium.click_button(HomeLocators.SEARCH_BUTTON)
        if self.selenium.page_should_contain("iphone 13"):
            pass

    def get_list_option(self):
        #self.selenium.click_button(HomeLocators.hamburger_btn)

        self.selenium.click_element("id=nav-hamburger-menu")
        #self.selenium.wait_until_element_is_visible("css:ul.hmenu-visible", timeout=5)
        #items = self.selenium.get_webelements("css:ul.hmenu-visible > li > a")
        #for item in items:
            #print("Menu Option:", item.text.strip())

        #sleep(1)
