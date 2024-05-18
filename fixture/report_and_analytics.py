import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table

class ReportAnalytics:
    add_folder_button = "i[class='oxd-svg-icon oxd-svg-icon--extra-large']"
    list_reports_name = '.reports-accordion-header-title p'
    add_report_name_field = 'input[placeholder="Enter Folder Name"]'
    save_folder_name = '//div[text()="Save"]'
    loading_spinner = '.oxd-loading-spinner'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_on_add_folder(self):
        self.step.click_on_element(self.add_folder_button, 1)

    def get_list_reports_name(self):
        return self.step.get_elements_texts(self.list_reports_name)

    def input_report_name(self, text):
        self.step.wait_for_element(self.add_report_name_field)
        self.step.input_text(self.add_report_name_field, text)

    def click_save_name_folder(self):
        self.step.click_on_element(self.save_folder_name, True)

    def wait_for_page_loading(self):
        self.step.specified_element_is_not_present(self.loading_spinner, 30)