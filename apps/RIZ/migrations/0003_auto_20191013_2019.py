# Generated by Django 2.2.2 on 2019-10-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RIZ', '0002_auto_20191013_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riz',
            name='col_stt',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='riz',
            name='num_USPD',
            field=models.IntegerField(default=1),
        ),
    ]
