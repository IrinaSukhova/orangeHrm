import time

import pytest


@pytest.mark.group3
def test_lesson_17_drag_and_drop(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Interactions", "Droppable",)
    app.demonstrationAppDemoQa.drag_and_drop()

@pytest.mark.group3
def test_lesson_17_drop_down_select(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Select Menu")
    app.demonstrationAppDemoQa.select_value_from_old_style_drop_down('White')

@pytest.mark.group3
def test_lesson_17_upload_file(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Upload and Download")
    app.demonstrationAppDemoQa.upload_file('/Users/admin/PycharmProjects/orangeHrm/files/test_upload.txt')

#-----------------------------------------------------------------------------------------
@pytest.mark.group3

def test_lesson_17_test_drag_and_drop2(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Interactions", "Dragabble")
    app.demonstrationAppDemoQa.drag_and_drop2()
    time.sleep(5)

    # go to "Interactions" "Dragabble" section
    # drag and drop the element to any position from the default from the page

@pytest.mark.group3
def test_lesson_17_test_drop_down_select(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Select Menu")
    app.demonstrationAppDemoQa.select_value_from_select_one_drop_down('Dr.')
    time.sleep(5)

    # select any other option from "Select One" drop-down

@pytest.mark.group3
def test_lesson_17_test_upload_file(app):
def test_lesson_17_2test_upload_file(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Upload and Download")
    app.demonstrationAppDemoQa.upload_file('C:/Users/isukhova/PycharmProjects/orangeHrm/files/test_uploadHome.txt')
        # Create some file in your project and upload it using upload method from previous example