# Generated by Django 3.1.1 on 2020-09-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200923_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftcards',
            name='user',
        ),
        migrations.AddField(
            model_name='giftcards',
            name='user',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]