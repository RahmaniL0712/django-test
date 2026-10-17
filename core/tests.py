from django.test import TestCase
from unittest.mock import patch


class ContactFormTests(TestCase):
    def test_contact_page_renders_form(self):
        response = self.client.get("/contact")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'method="post"')
        self.assertContains(response, "csrfmiddlewaretoken")
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="message"')

    @patch("builtins.print")
    def test_valid_post_prints_submitted_values(self, mock_print):
        response = self.client.post("/contact", {
            "name": "Ada",
            "email": "ada@example.com",
            "message": "Hello there",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mesazhi juaj u regjistrua me sukses")
        mock_print.assert_called_once_with("Contact form submission:", {
            "name": "Ada",
            "email": "ada@example.com",
            "message": "Hello there",
        })

    @patch("builtins.print")
    def test_invalid_post_shows_errors_without_printing(self, mock_print):
        response = self.client.post("/contact", {
            "name": "Ada",
            "email": "not-an-email",
            "message": "Hello there",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")
        mock_print.assert_not_called()
