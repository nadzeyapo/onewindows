# Generated by Django 5.1.7 on 2025-03-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='Без названия', max_length=2000),
        ),
    ]
