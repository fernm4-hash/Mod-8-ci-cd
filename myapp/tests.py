from django.test import TestCase

# Create your tests here.

#add tests for your views and models here.

class MyAppTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")

    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Page")

    def test_api_hello_view(self):
        response = self.client.get('/api/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, API!", "course": "CSC 325"})