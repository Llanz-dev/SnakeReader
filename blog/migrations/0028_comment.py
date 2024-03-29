# Generated by Django 4.0.6 on 2022-09-18 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_profile_user'),
        ('blog', '0027_alter_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, max_length=70, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('author_profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
