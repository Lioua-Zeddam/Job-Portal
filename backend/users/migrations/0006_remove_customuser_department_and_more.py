# Generated by Django 5.1.4 on 2025-01-19 12:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.AddField(
            model_name='otpverification',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='otpverification',
            name='otp',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='otpverification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
