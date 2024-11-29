# Generated by Django 5.1.2 on 2024-11-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='unknown', max_length=15),
            preserve_default=False,
        ),
    ]
