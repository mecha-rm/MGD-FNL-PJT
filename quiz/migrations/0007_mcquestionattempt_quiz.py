# Generated by Django 2.1.5 on 2019-01-27 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_mcquestionattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcquestionattempt',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]