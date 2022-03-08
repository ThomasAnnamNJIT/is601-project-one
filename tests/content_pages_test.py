
def test_request_index(client):
    """This makes the index page request"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link active" aria-current="page" href="#">Home</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/github">GitHub</a>' in response.data
    assert b'<a class="nav-link" href="/python">Python/Flask</a>' in response.data


def test_request_docker_page(client):
    """This makes the docker page request"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<a class="nav-link active" href="#">Docker</a>' in response.data


def test_request_github_page(client):
    """This makes the docker page request"""
    response = client.get("/github")
    assert response.status_code == 200
    assert b'<a class="nav-link active" href="#">GitHub</a>' in response.data


def test_request_python_page(client):
    """This makes the python page request"""
    response = client.get("/python")
    assert b'<a class="nav-link active" href="#">Python/Flask</a>' in response.data
