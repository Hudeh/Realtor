# Generated by Django 2.1.5 on 2019-02-03 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='location',
            new_name='locations',
        ),
    ]
