from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Substring 'login' is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password_confirmation = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_email.send_keys(email)
        registration_password.send_keys(password)
        registration_password_confirmation.send_keys(password)
        registration_submit.click()
