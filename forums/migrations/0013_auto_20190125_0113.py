# Generated by Django 2.1.5 on 2019-01-25 01:13

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0012_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]