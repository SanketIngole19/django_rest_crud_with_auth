# Generated by Django 5.0.2 on 2024-02-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs", name="content", field=models.TextField(),
        ),
    ]