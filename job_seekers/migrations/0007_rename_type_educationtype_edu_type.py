# Generated by Django 5.0.7 on 2024-11-15 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0006_educationtype_levelforedu_alter_skills_skill_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationtype',
            old_name='type',
            new_name='edu_type',
        ),
    ]
