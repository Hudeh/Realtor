# Generated by Django 2.1.3 on 2019-01-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_contactform_listing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='listing_id',
            field=models.IntegerField(default=0),
        ),
    ]
