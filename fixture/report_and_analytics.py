import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table

class ReportAnalytics:
    add_folder_button = "i[class='oxd-svg-icon oxd-svg-icon--extra-large']"
    list_reports_name = '.reports-accordion-header-title p'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_on_add_folder(self):
        self.step.click_on_element(self.add_folder_button, 1)

    def get_list_reports_name(self):
        return self.step.get_elements_texts(self.list_reports_name)
