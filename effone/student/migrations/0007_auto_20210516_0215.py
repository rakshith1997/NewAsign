# Generated by Django 3.2.2 on 2021-05-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('student', '0006_auto_20210513_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]