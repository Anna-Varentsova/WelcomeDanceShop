# Generated by Django 4.2.1 on 2023-06-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_gender_options_alter_goods_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='slug',
            field=models.SlugField(max_length=255, null=True, verbose_name='URL'),
        ),
    ]