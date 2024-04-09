import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '#ribbon-actions ui-view a'
    filtered_usernames = 'tbody td:nth-child(2) span'
    filtered_user_roles = 'tbody td:nth-child(3) span'
    filter_no_records_message = '//div[text()="No Records Found"]'
    save_button = '#modal-save-button'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    first_table_row = '#systemUserDiv tbody tr:nth-child(1)'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_add_user(self):
        self.step.specified_element_is_present(self.add_user_button, 30)
        self.step.click_on_element(self.add_user_button)
        self.step.wait_for_element(self.save_button)


    def get_filtered_usernames(self):
        return self.step.get_elements_texts(self.filtered_usernames)

    def get_filtered_user_role(self):
        return self.step.get_elements_texts(self.filtered_user_roles)

    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message,2)
        return self.step.get_element_text(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message, 5)
        return self.step.specified_element_is_present(self.filtered_usernames)

    def get_list_of_user_names(self):
        time.sleep(3)
        return self.step.get_elements_texts(self.filtered_usernames)

    def click_filter(self):
        self.step.wait_for_element(self.first_table_row,40)
        self.step.click_on_element(self.filter_users_button, 1)

    def get_filter_no_records_message_text(self):
        return self.step.get_element_text(self.filter_no_records_message)

    def is_list_of_users_displayed(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message, 5)
        return self.step.specified_element_is_present(self.filtered_usernames)