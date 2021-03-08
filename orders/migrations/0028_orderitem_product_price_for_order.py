# Generated by Django 3.1.5 on 2021-02-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20210203_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_price_for_order',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Product Price Used'),
        ),
    ]
