import pytest

from zajecia_12.my_module import add_numbers, calculate_net_salary

@pytest.fixture
def sample_user():
    return {
        "name": "Michał",
        "surname":  "Ziętkowski",
        "gross_salary": 3500,
        "age": 30,
    }

@pytest.fixture
def user_without_salary():
    return {
        "name": "Anna",
        "surname": "Kowalska",
        "age": 28,
    }

@pytest.fixture
def expected_net_salaries():
    return {
        "month_1": 3080.0,
        "month_2": 3080.0,
        "month_3": 3080.0,
        "month_4": 3080.0,
        "month_5": 3080.0,
        "month_6": 3080.0,
        "month_7": 3080.0,
        "month_8": 3080.0,
        "month_9": 3080.0,
        "month_10": 3080.0,
        "month_11": 3080.0,
        "month_12": 3080.0
    }



@pytest.mark.parametrize("a, b, expected",
                         [
                             (2, 3, 5),
                             (-1, 1, 0),
                             (0, 0, 0),
                             (10, 15, 25),
                             (-5, -5, -10)
                         ])
def test_add_numbers(a, b, expected):
    # assert add_numbers(2, 3) == 5
    # assert add_numbers(-1, 1) == 0
    # assert add_numbers(0, 0) == 0
    assert add_numbers(a, b) == expected


def test_calculate_net_salary_below_threshold(sample_user, expected_net_salaries):
    assert calculate_net_salary(sample_user) == expected_net_salaries

def test_calculate_net_salary_above_threshold():
    user = {
        "name": "Test",
        "surname": "User",
        "gross_salary": 12000,
        "age": 40,
    }
    expected_net_salaries = {
        "month_1": 8160.0,
        "month_2": 8160.0,
        "month_3": 8160.0,
        "month_4": 8160.0,
        "month_5": 8160.0,
        "month_6": 8160.0,
        "month_7": 8160.0,
        "month_8": 8160.0,
        "month_9": 8160.0,
        "month_10": 8160.0,
        "month_11": 8160.0,
        "month_12": 8160.0
    }
    assert calculate_net_salary(user) == expected_net_salaries

def test_calculate_net_salary_raises_exception_for_missing_gross_salary(user_without_salary):
    with pytest.raises(TypeError):
        calculate_net_salary(user_without_salary)