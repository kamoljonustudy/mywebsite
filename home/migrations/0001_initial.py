# Generated by Django 5.1.4 on 2024-12-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywoards', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=550)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('smpt_server', models.CharField(max_length=255)),
                ('smpt_email', models.CharField(max_length=255)),
                ('smpt_password', models.CharField(max_length=255)),
                ('smpt_port', models.CharField(max_length=255)),
                ('youtube', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='images/')),
                ('aboutus', models.TextField(max_length=550)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
    ]