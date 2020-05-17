from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.auth_token.models import Token
from rest_framework.test import APITestCase

from .views import RegistrationAPIView, LoginAPIView, TokenAPIView


class RegistrationAPIViewTestCase(APITestCase):
	pass


class LoginAPIViewTestCase(APITestCase):
	pass


class TokenAPIViewTestCase(APITestCase):
	pass