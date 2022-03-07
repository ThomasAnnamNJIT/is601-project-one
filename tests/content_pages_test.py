
def test_request_index(client):
    """This makes the index page request"""
    response = client.get("/")
    assert response.status_code == 200