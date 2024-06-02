from typing import Any, Callable, Iterable

from services import constants
from streamlit.testing.v1 import AppTest

# see  https://docs.streamlit.io/develop/concepts/app-testing

APP_PATH = "src/pages/0_first_page.py"


def find_widget(widgets_list: Iterable, condition: Callable) -> Any:
    for widget in widgets_list:
        if condition(widget):
            return widget
    raise ValueError("Widget not found")


def login(at: AppTest, password: str) -> None:
    password_field = find_widget(at.text_input, lambda x: x.label == "Password")
    password_field.set_value(password)
    submit_button = find_widget(at.button, lambda x: x.label == "Submit")
    submit_button.click().run()


def test_login() -> None:
    at = AppTest.from_file(APP_PATH).run()

    login(at, "wrong_password")
    error = find_widget(at.error, lambda x: x.value == "Not authenticated")
    assert error is not None

    login(at, constants.APP_PASSWORD)
    toast = find_widget(at.toast, lambda x: x.value == "✅ Logged in")
    assert toast is not None
    assert at.session_state.authenticated == True


def test_text() -> None:
    at = AppTest.from_file(APP_PATH).run()
    login(at, constants.APP_PASSWORD)

    some_header = find_widget(at.markdown, lambda x: "##" in x.value)
    assert some_header is not None


def test_slider() -> None:
    at = AppTest.from_file(APP_PATH).run()
    login(at, constants.APP_PASSWORD)

    slider = find_widget(at.slider, lambda x: x.label == "Slider")
    assert slider.value == 50
    descriptive_text = find_widget(
        at.markdown,
        lambda x: x.value == "The slider value is `50`",
    )
    assert descriptive_text.value == "The slider value is `50`"
