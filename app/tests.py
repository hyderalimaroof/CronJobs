from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse
from django.test import TestCase


class EmailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_send_email_successfully(self):
        res = self.client.post(reverse('send_email'))
        self.assertEqual(
            res.status_code,
            status.HTTP_200_OK
        )
