# Generated by Django 4.1.1 on 2022-10-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="first_message",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="fourth_message",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="second_message",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="third_message",
            field=models.TextField(blank=True, null=True),
        ),
    ]