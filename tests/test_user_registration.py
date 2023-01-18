import allure
from demoqa_tests.model.pages import practice_form


@allure.title("Successful fill form")
def test_student_registration_form():
    with allure.step("Open registration form"):
        practice_form.given_opened()

    # WHEN
    with allure.step("Fill form"):
        practice_form.set_name('Test')
        practice_form.set_last_name('Testov')
        practice_form.set_email('test@gmail.com')
        practice_form.set_gender('Female')
        practice_form.set_phone_number('1234567890')
        practice_form.set_birthday('5', '1995', '24')
        practice_form.set_subjects('Computer Science')
        practice_form.set_hobbies('Reading')
        practice_form.picture_upload('resources/foto.jpg')
        practice_form.set_address('Saratovskaya 19')
        practice_form.scroll_to_bottom()
        practice_form.set_state('NCR')
        practice_form.set_city('Delhi')

        practice_form.submit()

    # THEN
    with allure.step("Check form results"):
        practice_form.should_have_submitted(
            [
                ('Student Name', 'Test Testov'),
                ('Student Email', 'test@gmail.com'),
                ('Mobile', '1234567890'),
                ('Date of Birth', '24 June,1995'),
                ('Subjects', 'Computer Science'),
                ('Hobbies', 'Reading'),
                ('Picture', 'foto.jpg'),
                ('Address', 'Saratovskaya 19'),
                ('State', 'NCR Delhi'),
            ],
        )