# Generated by Django 4.1.1 on 2022-10-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_productpage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('PR', 'Programming'), ('DE', 'Designing'), ('FI', 'Financial')], max_length=2)),
                ('message', models.TextField()),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('inquiry_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-inquiry_at'],
            },
        ),
    ]
