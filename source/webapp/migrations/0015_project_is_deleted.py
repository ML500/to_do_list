# Generated by Django 2.2 on 2020-08-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20200825_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Мягкое удаление'),
        ),
    ]
