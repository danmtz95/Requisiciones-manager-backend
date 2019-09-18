# Generated by Django 2.2.5 on 2019-09-18 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requisiciones', '0008_auto_20190911_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_compra', models.CharField(max_length=150)),
                ('rastreo', models.CharField(max_length=150)),
                ('costo', models.FloatField()),
                ('proveedores', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('requisicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.Requisicion')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
