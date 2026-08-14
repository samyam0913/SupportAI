import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_register_creates_user(api_client):
    response = api_client.post(
        reverse("auth-register"),
        {
            "email": "owner@acme.test",
            "password": "S3cure!Pass123",
            "full_name": "Ada Owner",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email="owner@acme.test").exists()

    # Password must never be returned in the response
    assert "password" not in response.data


@pytest.mark.django_db
def test_register_rejects_duplicate_email(api_client):
    User.objects.create_user(
        email="owner@acme.test",
        password="S3cure!Pass123",
    )

    response = api_client.post(
        reverse("auth-register"),
        {
            "email": "owner@acme.test",
            "password": "AnotherPass123!",
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_returns_tokens(api_client):
    User.objects.create_user(
        email="owner@acme.test",
        password="S3cure!Pass123",
    )

    response = api_client.post(
        reverse("auth-login"),
        {
            "email": "owner@acme.test",
            "password": "S3cure!Pass123",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_me_requires_authentication(api_client):
    response = api_client.get(reverse("auth-me"))

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_me_returns_current_user(api_client):
    user = User.objects.create_user(
        email="owner@acme.test",
        password="S3cure!Pass123",
    )

    api_client.force_authenticate(user=user)

    response = api_client.get(reverse("auth-me"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == "owner@acme.test"


@pytest.mark.django_db
def test_logout_blacklists_refresh_token(api_client):
    user = User.objects.create_user(
        email="owner@acme.test",
        password="S3cure!Pass123",
    )

    login = api_client.post(
        reverse("auth-login"),
        {
            "email": "owner@acme.test",
            "password": "S3cure!Pass123",
        },
    )

    refresh = login.data["refresh"]

    api_client.force_authenticate(user=user)

    logout = api_client.post(
        reverse("auth-logout"),
        {"refresh": refresh},
    )

    assert logout.status_code == status.HTTP_205_RESET_CONTENT

    # The same refresh token must now be rejected
    retry = api_client.post(
        reverse("auth-refresh"),
        {"refresh": refresh},
    )

    assert retry.status_code == status.HTTP_401_UNAUTHORIZED