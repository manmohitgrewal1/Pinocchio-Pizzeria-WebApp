# Generated by Django 3.0.6 on 2020-05-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200526_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(default='', max_length=50),
        ),
    ]