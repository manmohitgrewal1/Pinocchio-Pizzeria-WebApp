# Generated by Django 3.0.6 on 2020-05-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200527_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='sub_topping',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.SubTopping'),
        ),
    ]