from programs.factorial import fact


def test_fact():
    assert fact(5) == 120
    # n * (n - 1 * ( n - 2 .... n times)


def test_fact2():
    assert fact(4) == 24


def test_fact3():
    assert fact(3) == 6


def test_fact4():
    assert fact(2) == 2
