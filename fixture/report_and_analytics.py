from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.step import StepHelper


class ReportAnalytics:
    add_folder_button = "i[class='oxd-svg-icon oxd-svg-icon--extra-large']"
    list_reports_name = '.reports-accordion-header-title p'
    add_report_name_field = 'input[placeholder="Enter Folder Name"]'
    save_folder_name = '//div[text()="Save"]'
    loading_spinner = '.oxd-loading-spinner'
    folder_manipulation_message = '//div[@class="oxd-toast-content oxd-toast-content--success"]/p[2]'
    folder_names_list = '//div[@class="reports-accordion-header-title"]/p'
    folder_delete_confirmation_header = '//p[text()="Are you sure?"]'
    folder_delete_confirm = '//div[text()="Yes, Delete"]'

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

    def get_manipulation_meassage_text(self):
        self.step.wait_for_element(self.folder_manipulation_message)
        return self.step.get_element_text(self.folder_manipulation_message)

    def find_and_click_delete_button_for_folder(self, random_name):
        folder_elements = self.step.wd.find_elements(By.XPATH, self.folder_names_list)
        for folder_element in folder_elements:
            if folder_element.text == random_name:
                delete_button = folder_element.find_element(By.XPATH, './following::div//button[@tooltip="Delete"]')
                delete_button.click()

    def confirm_folder_deleting(self):
        self.step.wait_for_element(self.folder_delete_confirmation_header)
        self.step.click_on_element(self.folder_delete_confirm)