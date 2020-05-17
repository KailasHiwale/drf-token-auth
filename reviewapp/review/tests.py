import json
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.auth_token.models import Token
from rest_framework.test import APITestCase

from .serializer import InstituteSerializer
from .views import InstituteListCreateAPIView, InstituteRetrieveUpdateDestroyAPIView


class InstituteListCreateAPIViewTestCase(APITestCase):
	pass



class InstituteRetrieveUpdateDestroyAPIViewTestCase(APITestCase):
	pass	



