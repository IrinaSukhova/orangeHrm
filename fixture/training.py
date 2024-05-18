from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table


class Training:
    filter_button = "a[id=searchModal]"
    add_course_button = "//i[text()='add']"
    iframe = "#noncoreIframe"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#resultTable tbody tr',
                           column_selectors={'check_box_list': '#resultTable td:nth-child(1)',
                                             'title': '#resultTable td:nth-child(2) a',
                                             'subunit': '#resultTable td:nth-child(3) a',
                                             'coordinator': '#resultTable td:nth-child(4) a',
                                             'company': '#resultTable td:nth-child(5) a',
                                             'status': '#resultTable td:nth-child(6) a'})

    def click_on_filter_button(self):
        self.step.switch_to_iframe(self.iframe)
        self.step.click_on_element(self.filter_button)
        self.step.switch_to_default_content()

    def click_on_add_course_button(self):
        self.step.click_on_element(self.add_course_button)
