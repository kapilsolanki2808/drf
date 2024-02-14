# Generated by Django 4.2.7 on 2024-02-02 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('content', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime(2024, 2, 2, 9, 42, 27, 537562))),
            ],
        ),
    ]
