# Generated by Django 3.0.7 on 2020-06-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20200615_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(help_text='Course description (max 800 characters)', max_length=800, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='course',
            name='description_fr',
            field=models.TextField(help_text='Course description (max 800 characters)', max_length=800, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_en',
            field=models.CharField(help_text='Course name (max 100 characters)', max_length=100, null=True, unique=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_fr',
            field=models.CharField(help_text='Course name (max 100 characters)', max_length=100, null=True, unique=True, verbose_name='name'),
        ),
    ]
