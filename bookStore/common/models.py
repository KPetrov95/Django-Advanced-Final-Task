from django.contrib.auth import get_user_model
from django.db import models

from bookStore import settings
from bookStore.mixins import TimestampMixin

UserModel = get_user_model()


class BookReview(TimestampMixin, models.Model):
    class Meta:
        ordering = ['-created_at']

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    book = models.ForeignKey(
        'catalog.Book',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    title = models.CharField(
        max_length=50,
        unique=True,
    )
    content = models.TextField(max_length=2000)
