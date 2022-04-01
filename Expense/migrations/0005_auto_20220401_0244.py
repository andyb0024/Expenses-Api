# Generated by Django 3.2.4 on 2022-04-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0004_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='item',
        ),
        migrations.AddField(
            model_name='income',
            name='source',
            field=models.CharField(choices=[('SALARY', 'SALARY'), ('BUSINESS', 'BUSINESS'), ('SIDE-HUSTLES', 'SIDE-HUSTLES'), ('OTHERS', 'OTHERS')], default=False, max_length=255),
        ),
    ]
