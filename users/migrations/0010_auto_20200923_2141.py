# Generated by Django 3.1.1 on 2020-09-23 19:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_auto_20200923_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftcards',
            name='user',
        ),
        migrations.AddField(
            model_name='giftcards',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]