from django.test import TestCase
import rest_framework.test as drf
from django.urls import reverse

from bookStore.accounts.models import AppUser, UserProfile
from bookStore.catalog.models import Genre, Author, Book


class BookstoreIntegrationTests(TestCase):
    def setUp(self):
        self.client = drf.APIClient()

        # Create a user and authenticate
        self.user = AppUser.objects.create_user(username='testuser', password='12admin34', email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)

        # Create test data
        self.genre = Genre.objects.create(name="FictionTest")
        self.author = Author.objects.create(first_name="Author", last_name="Name")
        self.book = Book.objects.create(
            title="Test Book",
            description="Description of test book",
            price=10.99,
            isbn="1234567890123",
            author=self.author,
            genre=self.genre
        )
    def test_reduce_cart_quantity_view(self):
        # Simulate adding items to the cart
        session = self.client.session
        session['cart'] = {str(self.book.id): {'quantity': 2}}
        session.save()

        response = self.client.post(reverse('reduce_quantity', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

        # Check the updated cart
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.book.id)]['quantity'], 1)

        # Reduce to zero and check if the item is removed
        response = self.client.post(reverse('reduce_quantity', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        cart = self.client.session['cart']
        self.assertNotIn(str(self.book.id), cart)
