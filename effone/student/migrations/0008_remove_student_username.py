# Generated by Django 3.2.2 on 2021-05-15 20:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('student', '0007_auto_20210516_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
