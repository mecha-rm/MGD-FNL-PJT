# Generated by Django 3.0.3 on 2020-06-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofile',
            name='original_name',
            field=models.TextField(blank=True, null=True, verbose_name='video file original name'),
        ),
    ]
