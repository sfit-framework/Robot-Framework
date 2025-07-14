from SeleniumLibrary import SeleniumLibrary

class LoginKeywords:
    def __init__(self):
        self.selenium = SeleniumLibrary()

    def open_amazon_homepage(self):
        self.selenium.open_browser("https://www.amazon.in", "chrome")
        self.selenium.maximize_browser_window()

    def click_sign_in(self):
        self.selenium.click_element("id=nav-link-accountList")

    def enter_email(self, email):
        self.selenium.input_text("id=ap_email_login", email)
        self.selenium.click_element("id=continue")

    def enter_password_and_login(self, password):
        self.selenium.input_text("id=ap_password", password)
        self.selenium.click_element("id=signInSubmit")