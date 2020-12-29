from django.contrib import admin
from mi_CandyMuebles.models import *

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    search_fields = ('nombre', 'descripcion')
admin.site.register(Categoria,CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','idproducto','short','destacado','precio')
    list_filter = ('destacado',)
    search_fields = ('nombre', 'short', 'descripcion','idproducto', )

admin.site.register(Producto,ProductoAdmin)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    list_filter = ('idgaleria',)
    search_fields = ('nombre', 'descripcion',)

admin.site.register(Galeria,GaleriaAdmin)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio')
    search_fields = ('nombre','precio' )

admin.site.register(Delivery,DeliveryAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nrodocumento','nombre','estatus')
    list_filter = ('nrodocumento','estatus')
    search_fields = ('nrodocumento','nombre','estatus',)

admin.site.register(Cliente,ClienteAdmin)


class TipodeEventoAdmin(admin.ModelAdmin):
    list_display = ('nombre','idTipodeEvento')
    list_filter = ('nombre','idTipodeEvento')
    search_fields = ('nombre',)
admin.site.register(TipodeEvento,TipodeEventoAdmin)


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('idpedido','nombre', 'direccion_domicilio', 'telefono','estado','total','total_delivery','Tipoevento_idTipodeEvento')
    list_filter = ('estado','Tipoevento_idTipodeEvento',)
    search_fields = ('idpedido','nombre',)
admin.site.register(Pedido,PedidoAdmin)

class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('iddescuento','codigoreferido','fecha_ini','fecha_fin','status',)
    list_filter = ('codigoreferido','status',)
    search_fields = ('idpedido','codigoreferido',)

admin.site.register(Descuento,DescuentoAdmin)

# class CarritoAdmin(admin.ModelAdmin):
#     list_display = ('idcarrito','total')
#     search_fields = ('idcarrito',) 
# admin.site.register(Carrito,CarritoAdmin)

# class CarritoHasProductosAdmin(admin.ModelAdmin):
#     list_display = ('idcarritohasproductos','subtotal')
#     search_fields = ('idcarritohasproductos',) 
# admin.site.register(Carritohasproductos,CarritoHasProductosAdmin)





