# Generated by Django 4.1.1 on 2022-10-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('alt', models.CharField(blank=True, max_length=50)),
                ('image_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
