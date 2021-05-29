from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_basket_button.click()

    def should_be_item_in_basket(self):
        self.should_be_adding_message()
        self.should_be_price_message()

    def should_be_adding_message(self):
        product_title_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        product_title_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_title_basket == product_title_page, \
            "Message about item in basket doesn't fit with product price."

    def should_be_price_message(self):
        product_price_basket = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT).text
        product_price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_AMOUNT).text
        assert product_price_basket == product_price_page, "Message about price doesn't fit with product price."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is yet presented, but should be disappeared"
