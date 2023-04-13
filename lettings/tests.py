import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestLettings:
    def test_lettings_index_should_return_200(self):
        client = Client()
        response = client.get(reverse("lettings_index"))
        print(response)
        assert response.status_code == 200

    def test_lettings_index_should_contains_title(self):
        client = Client()
        response = client.get(reverse("lettings_index"))
        assert b"Lettings" in response.content
