from django.db import models

from bookStore.accounts.models import AppUser
from bookStore.catalog.models import Book
from bookStore.mixins import TimestampMixin


# Create your models here.
class Order(TimestampMixin, models.Model):
    user = models.ForeignKey(to=AppUser, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
