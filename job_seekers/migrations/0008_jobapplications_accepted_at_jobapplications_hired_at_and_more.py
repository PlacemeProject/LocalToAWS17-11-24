# Generated by Django 5.0.7 on 2024-11-16 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0007_rename_type_educationtype_edu_type'),
        ('recruiters', '0003_rename_country_countryforloc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplications',
            name='accepted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='hired_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='recruiters.jobs'),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='offered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='rejected_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='selected_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='shortlisted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='viewed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
