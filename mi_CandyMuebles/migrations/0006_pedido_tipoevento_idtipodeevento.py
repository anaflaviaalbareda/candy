# Generated by Django 3.0.6 on 2020-12-21 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi_CandyMuebles', '0005_producto_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='Tipoevento_idTipodeEvento',
            field=models.ForeignKey(db_column='Tipoevento_idTipodeEvento', default=1, on_delete=django.db.models.deletion.CASCADE, to='mi_CandyMuebles.TipodeEvento'),
            preserve_default=False,
        ),
    ]