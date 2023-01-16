from selene import have


def set_value(elements, text):
    elements.element_by(have.value(text)).element('..').click()