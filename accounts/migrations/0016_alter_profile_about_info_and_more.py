# Generated by Django 4.0.6 on 2022-08-07 08:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_profile_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_info',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_description',
            field=models.TextField(),
        ),
    ]
