# Generated by Django 4.2.1 on 2023-08-10 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_articles_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='user',
        ),
    ]