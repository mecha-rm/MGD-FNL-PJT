# Generated by Django 3.0.3 on 2020-04-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0032_auto_20200428_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcanswer',
            options={'verbose_name': 'Multiple Choice Answer', 'verbose_name_plural': 'Multiple Choice Answers'},
        ),
    ]