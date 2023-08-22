# Generated by Django 4.1.3 on 2023-08-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='image/articles')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updeted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]