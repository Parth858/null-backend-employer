# Generated by Django 4.2.3 on 2023-07-09 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POSTEmployer', '0002_job_delete_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='created_at',
        ),
    ]
