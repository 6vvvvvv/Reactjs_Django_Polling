# Generated by Django 3.0.4 on 2020-08-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_auto_20200827_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polling',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
