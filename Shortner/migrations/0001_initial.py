# Generated by Django 4.2.1 on 2023-05-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('sno', models.BigAutoField(primary_key=True, serialize=False)),
                ('olink', models.CharField(max_length=500)),
                ('short', models.CharField(max_length=200)),
            ],
        ),
    ]
