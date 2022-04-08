from tests import client

def test_home_title(client):
    response = client.get("/")
    html = response.data.decode()
    assert "URL Shortener" in html

def test_home_form_label(client):
    response = client.get("/")
    html = response.data.decode()
    assert "Website URL" in html
    assert "Short Name" in html
    assert "Shorten" in html

def test_home_form_type(client):
    response = client.get("/")
    html = response.data.decode()
    assert 'type="url"' in html
    assert 'type="text"' in html
    assert 'type="submit"' in html

