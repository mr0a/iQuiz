# Generated by Django 2.1.5 on 2019-01-30 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190129_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='draft_statement',
            field=models.TextField(default='Question statement', null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='updatedOn',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
