# Generated by Django 4.0.6 on 2022-08-13 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_profile_is_email_verfied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_email_verfied',
        ),
    ]