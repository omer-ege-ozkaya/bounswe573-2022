from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


# todo Shall we get rid of this repetition?
class HomePageTests(SimpleTestCase):
    page_url = "/"

    def test_url_by_name_is_correct(self):
        self.assertEqual(reverse("home_page_url"), self.page_url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get(self.page_url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(self.page_url)
        self.assertTemplateUsed(response, "home_page.html")

    def test_template_content(self):
        response = self.client.get(self.page_url)
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutPageTests(SimpleTestCase):
    page_url = "/about/"

    def test_url_by_name_correct(self):
        self.assertEqual(reverse("about_page_url"), self.page_url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get(self.page_url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_is_correct(self):
        response = self.client.get(self.page_url)
        self.assertTemplateUsed(response, "about_page.html")

    def test_template_content(self):
        response = self.client.get(self.page_url)
        self.assertContains(response, "<h1>About</h1>")

