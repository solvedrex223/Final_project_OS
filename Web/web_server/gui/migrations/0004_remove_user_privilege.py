# Generated by Django 3.1 on 2020-08-25 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0003_auto_20200823_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='privilege',
        ),
    ]
