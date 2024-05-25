from selenium.webdriver.remote.webdriver import WebDriver

from fixture.step import StepHelper
from fixture.table import Table


class Training:
    filter_button = "a[id='searchModal']"
    add_course_button = "//i[text()='add']"
    iframe = "#noncoreIframe"
    loading_spinner = 'div[class="center-align loading"]'
    save_message = '//div[@class="toast-message"]'
    go_to_courses_button = 'a[class="tooltipped go-back-menu-item"]'
    filter_spinner = '#preloader .gap-patch'



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
        self.step.click_on_element(self.filter_button)


    def click_on_add_course_button(self):
        self.step.click_on_element(self.add_course_button)

    def wait_for_page_loading(self):
        self.step.specified_element_is_not_present(self.loading_spinner, 30)

    def get_save_confirmation_message(self):
        self.step.wait_for_element(self.save_message, 20)
        return self.step.get_element_text(self.save_message)

    def click_on_go_to_courses_button(self):
        self.step.click_on_element(self.go_to_courses_button)

    def wait_filtered_table(self):
        self.step.specified_element_is_not_present(self.filter_spinner,20)

