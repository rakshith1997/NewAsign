# Generated by Django 3.2.2 on 2021-05-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('student', '0002_student_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='password2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
