# Generated by Django 4.0.4 on 2022-04-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Khalti', 'Khalti')], default='Cash On Delivery', max_length=20),
        ),
    ]
