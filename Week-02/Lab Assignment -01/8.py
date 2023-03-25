import pytest

def make_upper(String):
    return String.upper()

def  make_capital(String):
    return String.capitalize()

def make_lower(String):
    return String.lower()


def test_script():
    string = "JafrulAlamTusar"
    assert make_upper(string) == "JAFRULALAMTUSAR"
    assert make_capital(string) == "Jafrulalamtusar"
    assert make_lower(string) == "jafrulalamtusar"
