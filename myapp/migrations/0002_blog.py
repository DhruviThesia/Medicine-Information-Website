# Generated by Django 4.2.4 on 2023-08-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField(max_length=200)),
                ('postby', models.CharField(max_length=20)),
            ],
        ),
    ]