# Generated by Django 5.0 on 2023-12-22 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_alter_subcategories_data_cate_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategories_data',
            name='cate_name',
        ),
    ]
