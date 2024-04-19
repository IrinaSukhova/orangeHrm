import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    gear_button = "(//i[text()='ohrm_settings'])[2]"
    my_widgets_tab = "span[class='nav-link active']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    list_of_configurations_texts = "//a[@ng-if='!menu.children && !!menu.uiSref && maxLevels <= 0']"
    list_widgets_names = "span[class='oxd-switch-label']"


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def click_gear_button(self):
        self.step.click_on_element(self.gear_button)

    def click_my_widgets_tab(self):
        self.step.click_on_element(self.my_widgets_tab)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def get_widgets_names(self):
        return self.step.get_elements_texts(self.list_widgets_names)
