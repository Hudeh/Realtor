# Generated by Django 2.1.3 on 2019-01-08 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20190108_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='listing_id',
        ),
    ]
