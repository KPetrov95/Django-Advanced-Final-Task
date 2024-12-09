from django.test import TestCase
from bookStore.catalog.models import Author


class AuthorModelTests(TestCase):

    def test_full_name(self):
        author = Author.objects.create(first_name="Ivan", last_name="Ivanov")
        self.assertEqual(author.full_name, "Ivan Ivanov")