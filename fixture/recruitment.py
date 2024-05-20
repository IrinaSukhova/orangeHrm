import time

from selenium.webdriver.remote.webdriver import WebDriver

from fixture.step import StepHelper
from fixture.table import Table


class Recruitment:
    header_loading_component = 'div[class="oxd-status-tab-panel-header"] div[class="oxd-skeleton --animate"]'
    add_candidate_button = 'button[tooltip="Add Candidate"]'
    search_field = 'input[data-test="autocompleteSelect"]'
    searching_text = "//div[text()=Searching...']"
    list_of_found_search_values = 'div[role="listbox"] div[role="option"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector= '.oxd-table-body .oxd-table-card',
                           column_selectors={'check_box': 'input[type="checkbox"]',
                                             'name': '.oxd-table-cell-link',
                                             'email': 'div[class="oxd-table-cell oxd-padding-cell"]:nth-child(4) div'})

    def wait_for_page_loaded(self):
        self.step.specified_element_is_present(self.header_loading_component, 5)
        self.step.specified_element_is_not_present(self.header_loading_component, 10)


    def click_add_candidate_button(self):
        self.wait_for_page_loaded()
        self.step.click_on_element(self.add_candidate_button)

    def set_and_search(self, text):
        self.step.input_text(self.search_field, text)
        self.step.wait_for_element(self.searching_text, 5)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        self.step.click_element_containing_text(self.list_of_found_search_values, text)