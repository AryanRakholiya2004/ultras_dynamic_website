# Generated by Django 5.0 on 2023-12-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('image', models.FileField(default='', upload_to='media/user_data/')),
            ],
        ),
    ]
