# Generated by Django 2.1.5 on 2019-02-11 22:41

from django.db import migrations, models
import quiz.models.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_response_submitted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'get_latest_by': 'start_time'},
        ),
        migrations.AddField(
            model_name='question',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quizsettings',
            name='timeBetweenAttempt',
            field=quiz.models.custom_fields.IntegerRangeField(default=0, help_text='Set the time between the two consecutive attempts.', null=True, verbose_name='Time Between Attempts'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.TextField(blank=True, default='{}'),
        ),
    ]
