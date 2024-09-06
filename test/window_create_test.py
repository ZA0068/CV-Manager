import pytest
from kivy.app import App
from src.main import CVReactor
from kivy.base import EventLoop

@pytest.fixture
def kivy_app():
    EventLoop.ensure_window()
    app = CVReactor()
    return app

def test_kivy_app_opening(kivy_app):
    app = kivy_app
    app.run()
    assert isinstance(app.root, App.get_running_app().root.__class__)
    assert app.root.text == "Hello, Kivy!"
