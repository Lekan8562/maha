# Generated by Django 5.0.3 on 2024-05-06 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_projectreply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectcomment',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Project Comments'},
        ),
        migrations.AlterModelOptions(
            name='projectreply',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Comment Replies'},
        ),
    ]
