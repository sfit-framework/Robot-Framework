from SeleniumLibrary import SeleniumLibrary
from time import sleep

class Login_ExtremeKeywords:
    def __init__(self):
        self.selenium = SeleniumLibrary()

    def open_extreme_homepage(self):
        self.selenium.open_browser("https://g2r1.qa.xcloudiq.com", "chrome")
        sleep(20)
        self.selenium.maximize_browser_window()

    def enter_email(self, email):
        self.selenium.wait_until_element_is_visible('//input[@data-automation-tag="automation-login-page-username-field"]')
        self.selenium.input_text('//input[@data-automation-tag="automation-login-page-username-field"]', email)
        #self.selenium.click_element("id=continue")

    def enter_password_and_login(self, password):
        self.selenium.wait_until_element_is_visible('//input[@data-automation-tag="automation-login-page-password-field"]')
        self.selenium.input_text('//input[@data-automation-tag="automation-login-page-password-field"]', password)
        self.selenium.capture_page_screenshot()
       # self.selenium.click_element("id=signInSubmit")

    def click_sign_in(self):
        self.selenium.click_element("//button[@data-automation-tag='automation-login-page-submit-btn']")
        sleep(10)
        self.selenium.capture_page_screenshot()

    def click_log_out(self):
        sleep(10)
        self.selenium.click_element('//div[@data-dojo-attach-point="accountInfoUsername"]')
        self.selenium.capture_page_screenshot()

