# Generated by Django 3.1.7 on 2023-01-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('kilo', 'kilo')], max_length=100),
        ),
    ]
