# Generated by Django 3.2 on 2022-10-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20221011_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
