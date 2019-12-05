# Generated by Django 2.2.2 on 2019-06-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('worker', models.CharField(blank=True, max_length=100)),
                ('phone_worker', models.CharField(blank=True, max_length=20)),
                ('remarks', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddIndex(
            model_name='customr',
            index=models.Index(fields=['name'], name='Customr_cus_name_91d54d_idx'),
        ),
        migrations.AddIndex(
            model_name='customr',
            index=models.Index(fields=['worker'], name='Customr_cus_worker_134527_idx'),
        ),
    ]