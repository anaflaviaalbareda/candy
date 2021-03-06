# Generated by Django 3.0.6 on 2020-12-15 22:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idcarrito', models.AutoField(db_column='idCarrito', primary_key=True, serialize=False)),
                ('total', models.IntegerField(blank=True, db_column='Total', null=True)),
            ],
            options={
                'db_table': 'Carrito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idcategoria', models.AutoField(db_column='idcategoria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('foto', models.FileField(db_column='Foto 1', upload_to='img/productos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('destacado', models.BooleanField(db_column='Destacado', default=False)),
            ],
            options={
                'db_table': 'Categoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(db_column='idCliente', primary_key=True, serialize=False)),
                ('tipo_documento', models.IntegerField(choices=[(1, 'DNI'), (2, 'RUC')], default=1)),
                ('nrodocumento', models.CharField(blank=True, db_column='Nro Documento', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=45, null=True)),
                ('estatus', models.CharField(blank=True, db_column='Estatus', max_length=45, null=True)),
                ('notas', models.TextField(blank=True, db_column='Notas', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('iddelivery', models.AutoField(db_column='idDelivery', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('precio', models.IntegerField(blank=True, db_column='Precio', null=True)),
            ],
            options={
                'db_table': 'Delivery',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('iddescuento', models.AutoField(db_column='idDescuento', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('idgaleria', models.AutoField(db_column='idgaleria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('foto', models.FileField(db_column='Foto 1', upload_to='img/productos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
            ],
            options={
                'db_table': 'Galeria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Politicas',
            fields=[
                ('idPoliticas', models.AutoField(db_column='idPoliticas', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('texto', models.CharField(blank=True, db_column='Texto', max_length=45, null=True)),
                ('titulo', models.CharField(blank=True, db_column='Titulo', max_length=45, null=True)),
                ('orden', models.CharField(blank=True, db_column='Orden', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Politicas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipodeEvento',
            fields=[
                ('idTipodeEvento', models.AutoField(db_column='idTipodeEvento', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
            ],
            options={
                'db_table': 'TipodeEvento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('short', models.CharField(blank=True, db_column='Short', max_length=45, null=True)),
                ('precio', models.IntegerField(blank=True, db_column='Precio', null=True)),
                ('precio_promocion', models.IntegerField(blank=True, db_column='Precio Promocion', null=True)),
                ('promocion', models.BooleanField(db_column='Promocion', default=False)),
                ('destacado', models.BooleanField(db_column='Destacado', default=False)),
                ('foto', models.FileField(db_column='Foto 1', upload_to='img/productos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('foto2', models.FileField(blank=True, db_column='Foto 2', null=True, upload_to='img/productos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('foto3', models.FileField(blank=True, db_column='Foto 3', null=True, upload_to='img/productos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('modelo', models.CharField(blank=True, db_column='Modelo', max_length=45, null=True)),
                ('codigo', models.CharField(blank=True, db_column='Codigo', max_length=45, null=True)),
                ('color', models.CharField(blank=True, db_column='Color', max_length=45, null=True)),
                ('material', models.CharField(blank=True, db_column='Material', max_length=45, null=True)),
                ('preventa', models.BooleanField(db_column='Pre venta', default=False)),
                ('activo', models.BooleanField(db_column='Activo', default=True)),
                ('categoria_idcategoria', models.ForeignKey(db_column='categoria_idcategoria', on_delete=django.db.models.deletion.CASCADE, to='mi_CandyMuebles.Categoria')),
            ],
            options={
                'db_table': 'Producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idpedido', models.AutoField(db_column='idPedido', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=45, null=True)),
                ('pedido', models.TextField(blank=True, db_column='Pedido', null=True)),
                ('estado', models.CharField(blank=True, db_column='Estado', max_length=45, null=True)),
                ('direccion_domicilio', models.CharField(blank=True, db_column='Dirección_Domicilio', max_length=255, null=True)),
                ('direccion_evento', models.CharField(blank=True, db_column='Dirección_Evento', max_length=255, null=True)),
                ('factura', models.TextField(blank=True, db_column='Factura', null=True)),
                ('notas', models.TextField(blank=True, db_column='Notas', null=True)),
                ('total', models.IntegerField(blank=True, db_column='Total', null=True)),
                ('total_delivery', models.IntegerField(blank=True, db_column='Total Delivery', null=True)),
                ('fecha_ini', models.DateField(blank=True, db_column='Fecha Inicio')),
                ('fecha_fin', models.DateField(blank=True, db_column='Fecha Fin')),
                ('status', models.CharField(blank=True, db_column='Estado Pedido', max_length=2)),
                ('cliente_idcliente', models.ForeignKey(db_column='Cliente_idCliente', on_delete=django.db.models.deletion.CASCADE, to='mi_CandyMuebles.Cliente')),
                ('delivery_iddelivery', models.ForeignKey(db_column='Delivery_idDelivery', on_delete=django.db.models.deletion.CASCADE, to='mi_CandyMuebles.Delivery')),
            ],
            options={
                'db_table': 'Pedido',
                'managed': True,
                'unique_together': {('idpedido', 'delivery_iddelivery', 'cliente_idcliente')},
            },
        ),
        migrations.CreateModel(
            name='Carritohasproductos',
            fields=[
                ('idcarritohasproductos', models.AutoField(db_column='idCarritoHasProductos', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, db_column='Cantidad', null=True)),
                ('subtotal', models.IntegerField(blank=True, db_column='Subtotal', null=True)),
                ('carrito_idcarrito', models.ForeignKey(db_column='Carrito_idCarrito', on_delete=django.db.models.deletion.CASCADE, to='mi_CandyMuebles.Carrito')),
                ('producto_idproducto', models.ForeignKey(db_column='Producto_idProducto', on_delete=django.db.models.deletion.CASCADE, to='mi_CandyMuebles.Producto')),
            ],
            options={
                'db_table': 'CarritoHasProductos',
                'managed': True,
                'unique_together': {('idcarritohasproductos', 'carrito_idcarrito', 'producto_idproducto')},
            },
        ),
    ]
