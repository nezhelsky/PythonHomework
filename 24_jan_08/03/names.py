def get_names(numbers):
    result = []
    for num in numbers:
        match num:
            case 1:
                num_name = ["one"]
            case 2:
                num_name = ["two"]
            case 3:
                num_name = ["three"]
            case 4:
                num_name = ["four"]
            case 5:
                num_name = ["five"]
            case 6:
                num_name = ["six"]
            case 7:
                num_name = ["seven"]
            case 8:
                num_name = ["eight"]
            case 9:
                num_name = ["nine"]
            case 0:
                num_name = ["zero"]
            case _:
                num_name = [""]
        result += num_name
    
    return result

def test_get_names():
    assert get_names([3, 5, 1]) == ["three", "five", "one"]
    assert get_names((3, 1)) == ["three", "one"]
    assert get_names((3, 11)) == ["three", ""]
    assert get_names([]) == []
    print('Test_Ok')

test_get_names()