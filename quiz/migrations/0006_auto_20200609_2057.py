# Generated by Django 3.0.3 on 2020-06-09 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200609_1726'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionGroupHeader',
        ),
        migrations.CreateModel(
            name='QuestionGroupHeader',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('quiz.question',),
        ),
    ]
