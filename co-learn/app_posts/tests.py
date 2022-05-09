from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    page_url = "posts/"

    def test_url_by_name_is_correct(self):
        self.assertEqual(reverse("post_page_url"), self.page_url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get(self.page_url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(self.page_url)
        self.assertTemplateUsed(response, "post_page.html")

    def test_template_content(self):
        response = self.client.get(self.page_url)
        self.assertContains(response, "<h1>Message Board</h1>")