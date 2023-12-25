def is_same_type(array=None):
    if not array:
        return False
    for item in array:
        if not type(item) is type(array[0]):
            return False
    return True

def test_is_same_type():
    assert is_same_type(["asdas", "retre", "fgdf"]) == True
    assert is_same_type([23, 45, 67]) == True
    assert is_same_type(["asdas", 43, "fgdf"]) == False
    assert is_same_type([True, "retre", 234]) == False
    assert is_same_type([]) == False
    assert is_same_type([(), (), ()]) == True
    print("Тест пройден")

test_is_same_type()