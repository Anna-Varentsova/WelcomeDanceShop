# Generated by Django 4.2.1 on 2023-08-17 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_alter_goods_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['-rubric'], 'verbose_name': 'товары', 'verbose_name_plural': 'Товары'},
        ),
    ]
