from hackernews_article import get_articulos

def test_gest_articulos():
    """Is the numeber or articles 3?"""
    articulos, response, list = get_articulos()
    assert len(articulos) == 3

def test_response():
    """Is the API response 200?"""
    articulos, response, list = get_articulos()
    assert response == 200

def test_list():
    """Is the API response 200?"""
    articulos, response, list = get_articulos()
    assert len(list) > 400
