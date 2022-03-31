"""This test the homepage"""


def test_request_index(client):
    """This makes the index page request"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link active" aria-current="page" href="#">Home</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/github">GitHub</a>' in response.data
    assert b'<a class="nav-link" href="/python">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/ci-cd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/terms">OOP Terminology</a>' in response.data
    assert b'<a class="nav-link" href="/oop">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/solid">Solid</a>' in response.data
    assert b'<a class="nav-link" href="/aaa">AAA</a>' in response.data


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


def test_request_ci_cd_page(client):
    """This makes the ci/cd page request"""
    response = client.get("/ci-cd")
    assert b'<a class="nav-link active" href="#">CI/CD</a>' in response.data


def test_request_oop_terminology(client):
    """This makes the oop terminology request"""
    response = client.get("/terms")
    assert b'<a class="nav-link active" href="#">OOP Terminology</a>' in response.data


def test_request_oop(client):
    """This makes the oop request"""
    response = client.get("/oop")
    assert b'<a class="nav-link active" href="#">OOP</a>' in response.data


def test_request_solid(client):
    """This makes the solid request"""
    response = client.get("/solid")
    assert b'<a class="nav-link active" href="#">Solid</a>' in response.data


def test_request_aaa(client):
    """This makes the AAA request"""
    response = client.get("/aaa")
    assert b'<a class="nav-link active" href="#">AAA</a>' in response.data


def test_page_not_found_request(client):
    """This makes a page not found request"""
    response = client.get("/invalid-page")
    assert response.status_code == 404
