# Generated by Django 3.2 on 2022-10-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_alter_orders_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_number',
            field=models.CharField(default=1234, max_length=150),
            preserve_default=False,
        ),
    ]
