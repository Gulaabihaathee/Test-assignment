# Generated by Django 2.0.5 on 2018-06-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0016_auto_20180618_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
