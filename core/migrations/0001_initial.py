# Generated by Django 5.1.4 on 2024-12-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TextModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=50)),
                ("text", models.TextField()),
            ],
        ),
    ]
