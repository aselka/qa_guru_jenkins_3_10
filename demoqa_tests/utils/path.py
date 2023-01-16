from selene.support.shared import browser
import os
import tests


def create_path(element, file):
    browser.element(element).set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), file))
    )