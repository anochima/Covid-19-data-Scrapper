# Generated by Django 3.0.6 on 2020-06-15 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0004_auto_20200613_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 14, 23, 48, 59, 222692))),
            ],
            options={
                'verbose_name_plural': 'Guideline',
            },
        ),
        migrations.DeleteModel(
            name='guidelines',
        ),
    ]
