# Generated by Django 4.1.6 on 2024-10-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("to_do", "To do"),
                    ("in_progress", "In  progress"),
                    ("done", "Done"),
                    ("archive", "Archive"),
                ],
                max_length=50,
            ),
        ),
    ]
