# Generated by Django 3.0.7 on 2020-06-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_section_blind_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='blind_data',
        ),
        migrations.AddField(
            model_name='course',
            name='blind_data',
            field=models.BooleanField(default=False, help_text='Defines if user data (e.g., name) should be visible or not.', verbose_name='blind data'),
        ),
    ]
