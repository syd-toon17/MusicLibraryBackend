# Generated by Django 4.0.3 on 2022-03-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
