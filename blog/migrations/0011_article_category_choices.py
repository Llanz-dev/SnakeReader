# Generated by Django 4.0.6 on 2022-07-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category_choices',
            field=models.CharField(choices=[('health', 'HEALTH'), ('sports', 'SPORTS'), ('finance', 'FINANCE'), ('technology', 'TECHNOLOGY'), ('fashion', 'FASHION'), ('travel', 'TRAVEL'), ('music', 'MUSIC')], default='health', max_length=10),
        ),
    ]
