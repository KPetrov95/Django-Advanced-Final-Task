from django.core.validators import RegexValidator
from django.db import models

from bookStore.mixins import TimestampMixin
from cloudinary.models import CloudinaryField


class Author(TimestampMixin, models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = CloudinaryField(
        blank=True,
        null=True,
        default='https://res.cloudinary.com/drbktnxop/image/upload/v1730624599/default-avatar-icon-of-social-media'
                '-user-vector_nac4sc.jpg'
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def total_books(self):
        return self.books.count()

    def __str__(self):
        return self.full_name


class Genre(TimestampMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    @property
    def total_books(self):
        return self.books.count()

    def __str__(self):
        return f'{self.name}'


class Book(TimestampMixin, models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cover = CloudinaryField(
        null=True,
        blank=True,
        default='https://res.cloudinary.com/drbktnxop/image/upload/v1730624632/Missing-book-cover_ixkada.jpg'
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}(\d{3})?$',
                message="ISBN must be either 10 or 13 digits"
            )
        ],
        help_text="Enter a valid 10 or 13 digit ISBN"
    )
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='books', null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, default=1, related_name='books', null=True)
    published_at = models.DateField(null=True, blank=True)

    @property
    def formatted_isbn(self):
        """Formats ISBN to a readable form with hyphens."""
        if len(self.isbn) == 13:
            # ISBN-13 format: 978-3-16-148410-0
            return f"{self.isbn[:3]}-{self.isbn[3]}-{self.isbn[4:6]}-{self.isbn[6:12]}-{self.isbn[12]}"
        elif len(self.isbn) == 10:
            # ISBN-10 format: 0-306-40615-2
            return f"{self.isbn[:1]}-{self.isbn[1:4]}-{self.isbn[4:9]}-{self.isbn[9]}"
        return self.isbn

    def __str__(self):
        return f'{self.title}'
