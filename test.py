import pytest


# Тест №1


def test_one():
    a = [1, 2, 3, 4, 5]
    try:
        assert a.index(6)
    except ValueError:
        pass


# Тест №2


def func_1(a):
    summa = 0
    for i in a:
        summa += i

    return summa


def test_two():
    a = [1, 2, 3]
    assert func_1(a) == 6


# Тест №3

def func_2(test_arg):
    return len(test_arg)


@pytest.mark.parametrize("test_arg, expected", [([1, 2, 3, 4], 4)])
def test_three(test_arg, expected):
    assert func_2(test_arg) == expected


# Тест №4


def test_four():
    a = {"a": 20, "b": 3}
    try:
        assert print(a["p"])
    except KeyError:
        pass

# Тест №5


def test_five():
    a = {"a": 20, "b": 3}
    assert a["a"] == 20


# Тест №6

def func_3(test_arg):
    return len(test_arg)


@pytest.mark.parametrize("test_arg, expected", [({"a": 20, "b": 3}, 2)])
def test_six(test_arg, expected):
    assert func_3(test_arg) == expected

