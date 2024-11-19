# Generated by Django 5.1.2 on 2024-11-16 17:38

import cloudinary.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('photo', cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/drbktnxop/image/upload/v1730624599/default-avatar-icon-of-social-media-user-vector_nac4sc.jpg', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cover', cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/drbktnxop/image/upload/v1730624632/Missing-book-cover_ixkada.jpg', max_length=255, null=True)),
                ('isbn', models.CharField(help_text='Enter a valid 10 or 13 digit ISBN', max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='ISBN must be either 10 or 13 digits', regex='^\\d{10}(\\d{3})?$')])),
                ('published_at', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='books', to='catalog.author')),
                ('genre', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='books', to='catalog.genre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
