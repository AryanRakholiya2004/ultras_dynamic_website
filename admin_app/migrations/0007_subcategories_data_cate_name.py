# Generated by Django 5.0 on 2023-12-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_subcategories_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories_data',
            name='cate_name',
            field=models.CharField(default='shoes', max_length=50),
        ),
    ]
