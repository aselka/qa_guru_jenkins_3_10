import os

from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model import controls
from demoqa_tests.model.controls import dropdown, modal, datepicker, checkbox, radiobutton
from demoqa_tests.utils import path

state = browser.element('#state')


def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_name(value):
    browser.element('#firstName').type(value)


def set_last_name(value):
    browser.element('#lastName').type(value)


def set_email(value):
    browser.element('#userEmail').type(value)


def set_gender(gender):
    radiobutton.set_value(browser.all('[name=gender]'), gender)


def set_phone_number(value):
    browser.element('#userNumber').type(value)


def set_birthday(month, year, day):
    datepicker.set_birthday_date(month, year, day)


def picture_upload(path_to_pic):
    path.create_path('#uploadPicture', path_to_pic)


def set_address(value):
    browser.element('#currentAddress').type(value)


def set_hobbies(hobby):
    checkbox.checkboxes_click(browser.all('[for^=hobbies-checkbox]'), hobby)


def set_subjects(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def set_state(value):
    dropdown.select(browser.element('#state'), value)


def set_city(value):
    dropdown.select(browser.element('#city'), value)


def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def submit():
    browser.element('#submit').perform(command.js.click)


def should_have_submitted(data):
    rows = controls.modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))