# Generated by Django 5.1.4 on 2025-01-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='submitted_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
