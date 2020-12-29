# Generated by Django 3.0.6 on 2020-12-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_CandyMuebles', '0006_pedido_tipoevento_idtipodeevento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipodeevento',
            options={'managed': True, 'ordering': ['nombre']},
        ),
        migrations.AddField(
            model_name='descuento',
            name='Monto',
            field=models.IntegerField(blank=True, db_column='Monto', default=0, null=True),
        ),
        migrations.AddField(
            model_name='descuento',
            name='codigoreferido',
            field=models.CharField(blank=True, db_column='CodigoReferido', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='descuento',
            name='descuento',
            field=models.IntegerField(blank=True, db_column='Descuento', null=True),
        ),
        migrations.AddField(
            model_name='descuento',
            name='fecha_fin',
            field=models.DateField(blank=True, db_column='Fecha Fin', null=True),
        ),
        migrations.AddField(
            model_name='descuento',
            name='fecha_ini',
            field=models.DateField(blank=True, db_column='Fecha Inicio', null=True),
        ),
        migrations.AddField(
            model_name='descuento',
            name='status',
            field=models.BooleanField(db_column='Status', default=True),
        ),
    ]