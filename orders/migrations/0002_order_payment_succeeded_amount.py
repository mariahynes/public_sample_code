# Generated by Django 3.1.5 on 2021-01-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_succeeded_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Payment Amount'),
        ),
    ]
