# Generated by Django 5.0 on 2023-12-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_product_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_data',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product_data',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
