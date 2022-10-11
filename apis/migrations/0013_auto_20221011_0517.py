# Generated by Django 3.2 on 2022-10-11 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0012_auto_20221011_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='apis.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apis.product'),
            preserve_default=False,
        ),
    ]