# Generated by Django 4.0.5 on 2022-07-02 01:40

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_addresses_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]