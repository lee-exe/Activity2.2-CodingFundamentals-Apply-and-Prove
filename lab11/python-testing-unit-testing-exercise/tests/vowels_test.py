from programs.vowels import vowels

def test_vowels():
    assert vowels("greetings") == 3


def test_vowels2():
    assert vowels("lentils") == 2


def test_vowels3():
    assert vowels("word") == 1


def test_vowels4():
    assert vowels("green") == 2

