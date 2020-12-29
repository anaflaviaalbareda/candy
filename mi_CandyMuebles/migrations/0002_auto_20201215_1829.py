# Generated by Django 3.0.6 on 2020-12-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_CandyMuebles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_fin',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_ini',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='status',
        ),
        migrations.AddField(
            model_name='carrito',
            name='status',
            field=models.CharField(blank=True, db_column='Estado Pedido', max_length=2),
        ),
        migrations.AddField(
            model_name='carritohasproductos',
            name='fecha_fin',
            field=models.DateField(blank=True, db_column='Fecha Fin', null=True),
        ),
        migrations.AddField(
            model_name='carritohasproductos',
            name='fecha_ini',
            field=models.DateField(blank=True, db_column='Fecha Inicio', null=True),
        ),
    ]
