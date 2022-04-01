# Generated by Django 4.0.3 on 2022-03-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
        migrations.AddField(
            model_name='expense',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]