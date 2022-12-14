# Generated by Django 4.1.1 on 2022-10-04 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('alt', models.CharField(blank=True, max_length=50)),
                ('image_url', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False, help_text='Active means this image will display first in carousel')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.productcard')),
            ],
        ),
    ]
