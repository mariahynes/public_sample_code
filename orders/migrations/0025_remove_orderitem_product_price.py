# Generated by Django 3.1.5 on 2021-02-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20210203_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_price',
        ),
    ]
