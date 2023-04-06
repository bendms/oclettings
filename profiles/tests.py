import pytest

from django.urls import reverse
from django.test import Client 

@pytest.mark.django_db
class TestProfiles():
    def test_profiles_index_should_return_200(self):
        client = Client()
        response = client.get(reverse("profiles_index"))
        print(response)
        assert response.status_code == 200
        
    def test_profiles_index_should_contains_title(self):
        client = Client()
        response = client.get(reverse("profiles_index"))
        assert b"Profiles" in response.content