# Generated by Django 2.1.5 on 2019-02-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20190214_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='response_timing',
            field=models.TextField(blank=True, default='{}', null=True),
        ),
    ]
