# Generated by Django 2.2.5 on 2019-09-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisiciones', '0010_auto_20190919_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='estatuscompras',
            name='concepto',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
