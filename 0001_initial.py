# Generated by Django 4.2.7 on 2024-01-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimages')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
