# Generated by Django 3.0.5 on 2020-05-22 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200522_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='fixedproduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.FixedProduct'),
        ),
    ]
