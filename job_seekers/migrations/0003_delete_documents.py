# Generated by Django 5.0.7 on 2024-10-17 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0002_candidates_profile_pic_candidates_resume'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Documents',
        ),
    ]