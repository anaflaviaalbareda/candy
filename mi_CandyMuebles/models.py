
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import FileExtensionValidator

#---------------------------------------------------------
#----------------------ZONA OUTLET------------------------
#---------------------------------------------------------


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idcategoria', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)
    foto = models.FileField(upload_to='img/productos', db_column='Foto 1', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])  # Field name made lowercase.
    destacado = models.BooleanField(db_column='Destacado', default=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Categoria'

    def __str__(self):
        # return "name" from translation
        return self.nombre


class Galeria(models.Model):
    idgaleria = models.AutoField(db_column='idgaleria', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)
    foto = models.FileField(upload_to='img/productos', db_column='Foto 1', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Galeria'

    def __str__(self):
        # return "name" from translation
        return self.nombre


class Producto(models.Model):
    # CAMPOS ANA
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    short = models.CharField(db_column='Short', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    precio_promocion = models.IntegerField(db_column='Precio Promocion', blank=True, null=True)  # Field name made lowercase.
    promocion = models.BooleanField(db_column='Promocion',default=False)  # Field name made lowercase.
    destacado = models.BooleanField(db_column='Destacado', default=False)  # Field name made lowercase.
    foto = models.FileField(upload_to='img/productos', db_column='Foto 1', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])  # Field name made lowercase.
    foto2 = models.FileField(upload_to='img/productos', db_column='Foto 2', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])], blank=True, null=True)  # Field name made lowercase.
    foto3 = models.FileField(upload_to='img/productos', db_column='Foto 3', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])], blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=45, blank=True, null=True)
    codigo = models.CharField(db_column='Codigo', max_length=45,blank=True, null=True)
    color = models.CharField(db_column='Color', max_length=45, blank=True, null=True)
    material = models.CharField(db_column='Material', max_length=45, blank=True, null=True)
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)
    # CAMPOS ADDICIONALES
    preventa = models.BooleanField(db_column='Pre venta',default=False)  
    activo = models.BooleanField(db_column='Activo',default=True)
    categoria_idcategoria = models.ForeignKey(Categoria, models.CASCADE, db_column='categoria_idcategoria')  # Field name made lowercase.   

    class Meta:
        managed = True
        db_table = 'Producto'

    def __str__(self):
        # return "name" from translation
        return self.nombre


class Carrito(models.Model):
    idcarrito = models.AutoField(db_column='idCarrito', primary_key=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Carrito'


class Carritohasproductos(models.Model):
    idcarritohasproductos = models.AutoField(db_column='idCarritoHasProductos', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.  
    subtotal = models.IntegerField(db_column='Subtotal', blank=True, null=True)  # Field name made lowercase.
    carrito_idcarrito = models.ForeignKey(Carrito, models.CASCADE, db_column='Carrito_idCarrito')  # Field name made lowercase.
    producto_idproducto = models.ForeignKey(Producto, models.CASCADE, db_column='Producto_idProducto')  # Field name made lowercase.
    fecha_ini = models.DateField(db_column='Fecha Inicio', blank=True, null=True)
    fecha_fin = models.DateField(db_column='Fecha Fin', blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'CarritoHasProductos'
        unique_together = (('idcarritohasproductos', 'carrito_idcarrito', 'producto_idproducto'),)


class Delivery(models.Model):
    iddelivery = models.AutoField(db_column='idDelivery', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Delivery'

    def __str__(self):
        # return "name" from translation
        return '%s - $ %s' %(self.nombre,self.precio)


class Politicas(models.Model):
    # TABLAS ANA
    idPoliticas = models.AutoField(db_column='idPoliticas', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)
    texto = models.CharField(db_column='Texto', max_length=45, blank=True, null=True)
    titulo = models.CharField(db_column='Titulo', max_length=45, blank=True, null=True)
    orden = models.CharField(db_column='Orden', max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Politicas'


class TipodeEvento(models.Model):
    # TABLAS ANA
    idTipodeEvento = models.AutoField(db_column='idTipodeEvento', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TipodeEvento'
        ordering = ['nombre']
    
    def __str__(self):
        # return "name" from translation
        return self.nombre


class Cliente(models.Model):
    STATUS_CHOICES =[(1, "DNI"), (2, "RUC")]
    ORDER_STATUS =[(1, "Buen Cliente"), (2, "Regular Cliente"), (3, "Pesimo Cliente")]
    idCliente = models.AutoField(db_column='idCliente', primary_key=True)
    tipo_documento = models.IntegerField(choices=STATUS_CHOICES, default=1)   
    nrodocumento = models.CharField(db_column='Nro Documento', max_length=45, blank=True, null=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)
    estatus = models.IntegerField(choices=ORDER_STATUS, default=1)   
    notas = models.TextField(db_column='Notas', max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Cliente'

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    # TABLAS ANA
    idpedido = models.AutoField(db_column='idPedido', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    #fecha pedido?........................
    pedido = models.TextField(db_column='Pedido', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)
    direccion_domicilio = models.CharField(db_column='Dirección_Domicilio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion_evento = models.CharField(db_column='Dirección_Evento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    factura = models.TextField(db_column='Factura', blank=True, null=True)  # Field name made lowercase.
    delivery_iddelivery = models.ForeignKey(Delivery, models.CASCADE, db_column='Delivery_idDelivery')  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.CASCADE, db_column='Cliente_idCliente')
    Tipoevento_idTipodeEvento = models.ForeignKey(TipodeEvento, models.CASCADE, db_column='Tipoevento_idTipodeEvento')
    # TABLAS ADDICIONALES
    notas = models.TextField(db_column='Notas', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    total_delivery = models.IntegerField(db_column='Total Delivery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Pedido'
        unique_together = (('idpedido', 'delivery_iddelivery','cliente_idcliente'),)


class PedidoDetalle(models.Model):
    idpedidodetalle = models.AutoField(db_column='idpedidodetalle', primary_key=True)  # Field name made lowercase.
    pedido_idpedido = models.ForeignKey(Pedido, models.CASCADE, db_column='Pedido_idpedido')  # Field name made lowercase.
    producto_idproducto = models.ForeignKey(Producto, models.CASCADE, db_column='Producto_idproducto')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.  
    fecha_ini = models.DateField(db_column='Fecha Inicio', blank=True, null=True)
    fecha_fin = models.DateField(db_column='Fecha Fin', blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PedidoDetalle'
        unique_together = (('idpedidodetalle', 'pedido_idpedido','producto_idproducto'),)


class Descuento(models.Model):
    iddescuento = models.AutoField(db_column='idDescuento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigoreferido = models.CharField(db_column='CodigoReferido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descuento = models.IntegerField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase.  
    fecha_ini = models.DateField(db_column='Fecha Inicio', blank=True, null=True)
    fecha_fin = models.DateField(db_column='Fecha Fin', blank=True, null=True)
    Monto = models.IntegerField(db_column='Monto', blank=True, null=True,default=0)  # Field name made lowercase.  
    status = models.BooleanField(db_column='Status',default=True)