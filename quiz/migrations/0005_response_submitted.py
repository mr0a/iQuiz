# Generated by Django 2.1.5 on 2019-02-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
