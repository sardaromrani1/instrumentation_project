# Generated by Django 5.1.6 on 2025-03-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('part_number', models.CharField(max_length=100, unique=True)),
                ('range', models.CharField(max_length=100)),
            ],
        ),
    ]
