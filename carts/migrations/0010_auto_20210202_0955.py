# Generated by Django 3.1.5 on 2021-02-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_cartitems_discount_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
