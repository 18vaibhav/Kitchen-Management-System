# Generated by Django 3.2.8 on 2021-10-06 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_delete_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]