# Generated by Django 3.0.5 on 2020-05-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20200522_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='total_due',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yardproduct',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]