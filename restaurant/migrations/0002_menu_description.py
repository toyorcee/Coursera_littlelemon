# Generated by Django 5.0.2 on 2024-02-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(default='none', max_length=1000),
        ),
    ]
