# Generated by Django 2.2.10 on 2020-03-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20200304_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
