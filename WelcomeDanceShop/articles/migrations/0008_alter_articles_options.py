# Generated by Django 4.2.1 on 2023-07-19 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_articles_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'статьи', 'verbose_name_plural': 'Статьи'},
        ),
    ]
