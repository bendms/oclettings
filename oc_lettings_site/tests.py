from django.urls import reverse
from django.test import Client


def test_dummy():
    assert 1


def test_index_should_return_200():
    client = Client()
    response = client.get(reverse("index"))
    print(response)
    assert response.status_code == 200


def test_index_should_contains_title():
    client = Client()
    response = client.get(reverse("index"))
    assert b"Welcome to Holiday Homes" in response.content
