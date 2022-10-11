# Generated by Django 3.2 on 2022-10-10 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_customers_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='product',
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.products')),
            ],
        ),
    ]
