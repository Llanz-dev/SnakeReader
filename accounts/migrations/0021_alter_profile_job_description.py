# Generated by Django 4.0.6 on 2022-08-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_profile_about_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job_description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]