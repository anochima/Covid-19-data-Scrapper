# Generated by Django 3.0.6 on 2020-06-27 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0019_auto_20200626_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 58, 18, 400881)),
        ),
    ]
