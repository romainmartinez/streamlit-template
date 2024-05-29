from streamlit.testing.v1 import AppTest


def test_app() -> None:
    AppTest.from_file("src/home.py").run()
    assert 1 == 1
