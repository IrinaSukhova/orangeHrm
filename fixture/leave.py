
from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class Leave:
    date_from = '//label[@for="from"]/.. //i[text()="date_range"]'
    date_to = '//label[@for="to"]/.. //i[text()="date_range"]'
    search_button = '//button[text()="Search"]'
    search_message = '.toast-message'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.DEFAULT)

    def open_calendar_from(self):
        self.step.click_on_element(self.date_from)

    def open_calendar_to(self):
        self.step.click_on_element(self.date_to)

    def wait_calendar_displayed(self):
        self.step.wait_for_element(self.date_from)

    def click_search_button(self):
        self.step.click_on_element(self.search_button)

    def get_search_message(self):
        self.step.wait_for_element(self.search_message)
        return self.step.get_element_text(self.search_message)


