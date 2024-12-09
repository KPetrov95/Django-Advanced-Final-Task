from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from bookStore.accounts.managers import AppUserManager
from bookStore.accounts.validators import PhoneDigitsValidator
from bookStore.catalog.models import Book


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(4)]
    )
    email = models.EmailField(
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AppUserManager()


UserModel = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(regex=r'^\+?\d{10,13}$')],
        blank=True,
        null=True,
    )
    favorite_books = models.ManyToManyField(
        to=Book,
        related_name='favorited_by',
        blank=True
    )

    def __str__(self):
        return self.user.username