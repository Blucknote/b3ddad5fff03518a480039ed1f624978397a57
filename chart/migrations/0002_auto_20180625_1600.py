# Generated by Django 2.0.6 on 2018-06-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart_row',
            name='published_date',
        ),
        migrations.AddField(
            model_name='chart_row',
            name='pub_date',
            field=models.TextField(blank=True),
        ),
    ]
