import pytest
from .temperature_explorer import App


@pytest.fixture(scope="module")
def app() -> App:
    app = App()
    app.load_data()
    return app

def test_coldest(app: App) -> None:
    assert app.get_lowest() == (676223, 2010.542)

def test_highest_flux(app: App) -> None:
    assert app.get_highest_fluctuation() == 735181

@pytest.mark.parametrize("start,end,expected_value", [
    (2000.001, 2000.456, 756020),
    (2018.0, 2019.9, 758064)
])
def test_date_spans(app: App, start: float, end: float, expected_value: int) -> None:
    assert app.get_highest_for_date_range(start, end) == expected_value