from programs.list_of_squares import los


def test_los1():
    assert los(1) == {1: 1}


def test_los2():
    assert los(2) == {1: 1, 2: 4}


def test_los3():
    assert los(3) == {1: 1, 2: 4, 3: 9}


def test_los4():
    assert los(4) == {1: 1, 2: 4, 3: 9, 4: 16}
