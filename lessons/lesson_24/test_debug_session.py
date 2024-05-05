from selenium.webdriver.common.by import By

# Demonstrate how to use debugger
def test_debugger_demonstration_usage(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Links")
    app.demonstrationAppDemoQa.click_home_button()
    app.step.switch_to_tab_by_url("https://demoqa.com/")
    page_banner = app.demonstrationAppDemoQa.get_page_banner()
    page_url = app.demonstrationAppDemoQa.get_home_page_url()
    app.assert_that(app.demonstrationAppDemoQa.get_page_banner()).is_equal_to("Selenium Online Training")
    app.assert_that(app.demonstrationAppDemoQa.get_home_page_url()).is_equal_to('https://demoqa.com/')

# PRACTICAL EXAMPLES:
def test_drag_and_drop_functionality(app):
    # Navigate to the draggable demo page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/dragabble")
    # Perform drag and drop on the specified element
    app.demonstrationAppDemoQa.drag_and_drop_dragabble()

def test_dropdown_menu_interaction(app):
    # Open the URL for the select menu page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/select-menu")
    # Select an item from the dropdown
    app.demonstrationAppDemoQa.select_value_from_select_one_dropdown("Dr.")

def test_dropdown_menu_interaction1(app):
    # Open the default URL set in the openUrl method
    app.demonstrationAppDemoQa.openUrl()
    # Navigate to the select menu page
    # app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Home")
    # Select 'White' from the dropdown menu
    app.demonstrationAppDemoQa.select_value_from_select_one_dropdown('Dr.')

def test_dropdown_menu_interaction2(app):
    # Navigate to the select menu page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/select-menu")
    # Select an item from the dropdown
    app.demonstrationAppDemoQa.select_value_from_select_one_dropdown('White')

def test_file_upload_functionality(app):
    # Navigate to the file upload page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/upload-download")
    # Upload a file using an absolute path
    app.demonstrationAppDemoQa.upload_my_file("/Users/admin/PycharmProjects/orangeHrm/files/test_upload.txt")

def test_navigation_to_home(app):
    # Open the main page of the site
    app.demonstrationAppDemoQa.openUrl()
    # Go to Links section
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Links")
    # Click the home button to navigate to the home page
    app.demonstrationAppDemoQa.click_home_button()
    # Assert the URL to check if it's correct
    app.assert_that(app.demonstrationAppDemoQa.get_home_page_url()).is_equal_to('https://demoqa.com/links')

def test_modal_dialog_interaction(app):
    # Open the modal dialogs page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/modal-dialogs")
    # Click to Open the small modal without checking if it's open
    app.demonstrationAppDemoQa.wd.find_element(By.ID, "showSmallModal").click()
    # Get the text from the modal title and store it
    modal_title_text = app.demonstrationAppDemoQa.wd.find_element(By.ID, "example-modal-sizes-title-sm").text
    # Assert that the modal title text matches expected text
    assert modal_title_text == 'Small Modal'