# Generated by Django 3.0.5 on 2020-05-22 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20200522_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixedproduct',
            options={'ordering': ['time']},
        ),
    ]
