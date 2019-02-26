# Generated by Django 2.1.5 on 2019-02-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20190214_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltiuser',
            name='email',
            field=models.CharField(blank=True, help_text='Email of the student if provided', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ltiuser',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the user if available/given.', max_length=100, null=True),
        ),
    ]
