# Generated by Django 3.0.6 on 2020-06-26 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0013_auto_20200625_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 23, 47, 25, 484712)),
        ),
        migrations.AlterField(
            model_name='globalcases',
            name='country_recovery',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='globalcases',
            name='country_total_cases',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='globalcases',
            name='country_total_deaths',
            field=models.CharField(max_length=60),
        ),
    ]
