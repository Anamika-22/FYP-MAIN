# Generated by Django 4.0.3 on 2022-04-22 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_remove_order_payment_completed_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
