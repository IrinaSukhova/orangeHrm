import time
# test_lesson_22_switch_to_tab
    # Open the url and go to  "ElementsElements", "Links" section
    #  Click on 'Home' link
    # Switch to the new openned tab by its link
    # TODO: Werify that you are one the home page
import pytest
Home = 'simpleLink'


def test_lesson_22_switch_to_tab(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Links")
    app.demonstrationAppDemoQa.home_button1()
    time.sleep(5)

