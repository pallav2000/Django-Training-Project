# Generated by Django 2.2 on 2020-05-24 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_image_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_field',
            new_name='cover',
        ),
    ]
