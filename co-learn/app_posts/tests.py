from django.test import TestCase
from django.urls import reverse
from .models import Post


class HomePageTests(TestCase):
    page_url = "/posts/"

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_by_name_is_correct(self):
        self.assertEqual(reverse("post_page_url"), self.page_url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get(self.page_url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(self.page_url)
        self.assertTemplateUsed(response, "post_page.html")

    def test_static_template_content(self):
        response = self.client.get(self.page_url)
        self.assertContains(response, "<h1>Message Board</h1>")

    def test_dynamic_template_content(self):
        response = self.client.get(self.page_url)
        self.assertContains(response, "This is a test!")

