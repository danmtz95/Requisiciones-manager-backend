# Generated by Django 2.2.5 on 2019-09-06 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('rfc', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=150)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]