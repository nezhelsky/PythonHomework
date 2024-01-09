
def get_square(a=None, b=None):
    if b is None:
        b = a
    if not type(a) in (int, float) or not type(b) in (int, float, None):
        return None
    return a*b


def test_get_square():
    assert get_square(2, 3) == 6
    assert get_square(3, 0) == 0
    assert get_square(3) == 9
    assert get_square(4.5) == 4.5*4.5
    assert get_square("ololo") == None
    assert get_square() == None
    assert get_square(4, "asasa") == None
    print("Тест пройден")

test_get_square()