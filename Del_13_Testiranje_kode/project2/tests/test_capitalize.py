import pytest
from helpers.capitalize import capital_case


def test_capital_case():
    assert capital_case("semafor") == "Semafor"


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)