from tests import client

def test_about_content(client):
    response = client.get("/about")
    html = response.data.decode()
    assert 'About URL Shortener' in html
