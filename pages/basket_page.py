from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no empty basket message"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FULL_BASKET), "There is item in basket, but shouldn't be"
