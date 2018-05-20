from challenge import get_text


def test_make_html():
    assert get_text() == '<p><strong>I code with PyBites</strong></p>'
