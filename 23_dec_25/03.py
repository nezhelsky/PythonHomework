def get_result_list(user_list):
    result = []
    if not type(user_list) is (list, tuple):
        user_list = [user_list]
    for i in range(len(user_list)):
        summ = "" if type(user_list[0]) is str else 0
        for x in user_list[0:i+1]:
            summ += x
        result.append(summ)
    return result
    


def test_get_result_list():
    assert get_result_list([10, 2, 3, 5]) == [10, 12, 15, 20]
    assert get_result_list([23, 22, 21]) == [23, 45, 66]
    assert get_result_list({"asds", "sdss", "ewwe"}) == ["asds", "asdssdss", "asdssdssewwe"]
    assert get_result_list([]) == []
    assert get_result_list([345]) == [345]
    print("Test passed")

test_get_result_list()