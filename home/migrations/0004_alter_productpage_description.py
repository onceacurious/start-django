# Generated by Django 4.1.1 on 2022-10-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_productpage_description_alter_productpage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='description',
            field=models.CharField(default='No description', max_length=50),
        ),
    ]
