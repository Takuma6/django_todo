# Generated by Django 3.0.3 on 2020-05-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200508_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, verbose_name='予定完了日時'),
        ),
    ]
