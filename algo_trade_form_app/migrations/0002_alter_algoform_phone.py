# Generated by Django 4.2.7 on 2024-01-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trade_form_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algoform',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
