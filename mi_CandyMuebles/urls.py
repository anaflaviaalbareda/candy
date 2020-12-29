from django.urls import path
from . import views

urlpatterns=[

	path('', views.index, name='index'),
	path('carrito/',views.carrito,name='carrito'),
	path('galeria/',views.galeria, name='galeria'),
	path('productos/',views.productos,name='productos'),
	path('item/',views.item,name='item'),
	path('realizar_pedido/',views.realizar_pedido,name='realizar_pedido'),
	path('sobre_nosotros/',views.sobre_nosotros, name='sobre_nosotros'),
	path('realizar_pedido2/',views.realizar_pedido2,name='realizar_pedido2'),	
	path('contacto/',views.contacto,name='contacto'),		
	path('add_carrito/',views.add_carrito,name='add_carrito'),	
	path('del_carrito/',views.del_carrito,name='del_carrito'),	
	path('consultaDisponibilidad/',views.consultaDisponibilidad,name='consulta_Disponibilidad'),
	path('busquedacliente/',views.busquedacliente,name='busquedacliente'),	
	path('ValidateCodigoDescuento/',views.ValidateCodigoDescuento,name='ValidateCodigoDescuento'),	

	# path('add_carrito/',views.add_carrito,name='add_carrito'),
	# path('carrito/',views.carrito,name='carrito'),
	# path('del_carrito/',views.del_carrito,name='del_carrito'),
	#
		
	# path('contacto/',views.contacto,name='contacto'),			
	
	# path('compra_exito/',views.compra_exito,name='exito'),
	# path('compra_fallo/',views.compra_fallo,name='fallo'),
	# path('compra_proceso/',views.compra_proceso,name='proceso'),
]