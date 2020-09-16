from django.test import TestCase
from rest_framework import status
# Create your tests here.
class SampleTestCase(TestCase):
    def printmsg(self):
        print("Hi, I am testing")
        self.assertEqual(status.HTTPS_200_OK)