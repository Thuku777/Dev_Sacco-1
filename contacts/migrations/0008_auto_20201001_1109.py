# Generated by Django 3.1 on 2020-10-01 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_address_statement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='whatsapp',
            new_name='youtube',
        ),
    ]
