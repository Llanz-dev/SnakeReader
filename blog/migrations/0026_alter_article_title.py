# Generated by Django 4.0.6 on 2022-08-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
