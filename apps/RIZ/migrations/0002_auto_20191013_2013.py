# Generated by Django 2.2.2 on 2019-10-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RIZ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riz',
            name='col_stt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='riz',
            name='num_USPD',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
