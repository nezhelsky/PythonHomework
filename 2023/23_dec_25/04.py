def count_words(text: str) -> dict:
    pass

def test_count_words():
    assert count_words("Rocking around a christmas tree") == {"Rocking":1, "around":1, "a": 1, "christmas":1, "tree":1}
    assert count_words("star Star star") == {"star":3}
    assert count_words("") == {}
    assert count_words() == {}