# Функция возвращает аббревиатуру от переданной строки
def get_abbr(phrase):
    abbr = ""
    my_list = phrase.split()
    for word in my_list:
        abbr = abbr + word[0]
    return abbr.upper()




def test_get_abbr():
    assert get_abbr('семь раз отмерь - один раз отрежь') == 'СРО-ОРО'
    assert get_abbr("don't repeat yourself") == 'DRY'
    assert get_abbr('') == ''
    print("Тест пройден")

test_get_abbr()
