# Generated by Django 2.2.5 on 2019-09-10 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisiciones', '0006_auto_20190909_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisicionestado',
            old_name='cateogoria',
            new_name='categoria',
        ),
    ]