# Generated by Django 4.2.1 on 2023-07-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_rubric_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='quantity',
            field=models.PositiveSmallIntegerField(null=1),
            preserve_default=1,
        ),
    ]
