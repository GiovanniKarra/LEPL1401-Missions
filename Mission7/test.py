import search


def test_get_words():
    assert search.get_words("Turmoil has engulfed the Galactic Republic.") ==\
           ["turmoil", "has", "engulfed", "the", "galactic", "republic"], "Petit exemple donné"


test_get_words()
