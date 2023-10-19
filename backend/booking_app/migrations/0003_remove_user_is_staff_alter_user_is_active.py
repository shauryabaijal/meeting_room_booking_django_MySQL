# Generated by Django 4.1 on 2023-10-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking_app", "0002_meetingroom_booking"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]