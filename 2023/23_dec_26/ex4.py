# Два слова похожи, если отличаются только одной буквой. Функция проверяет, похожи строки, или нет.
def is_similar(word1=None, word2=None):
    if word2 is None:
        return False
    elif abs(len(word1) - len(word2)) == 1:
        return True
    elif abs(len(word1) - len(word2)) > 1:
        return False
    else:
        i = len(word1)
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count < 2:
            return True
        return False




def test_is_similar():
    assert is_similar('пень', 'лень') == True
    assert is_similar('вторник', 'вторнек') == True
    assert is_similar('город', 'огород') == True
    assert is_similar('перец', 'конец') == False
    assert is_similar('вор', 'ворон') == False
    assert is_similar('перец') == False
    print("Тест пройден")

test_is_similar()
