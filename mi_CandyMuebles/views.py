from django.shortcuts import render, redirect

import mercadopago
import json

from .models import *
from .forms import Formulario_Crear_Nuevo

from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
import requests


from numpy import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
import random
import hmac
import hashlib
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import socket
from datetime import datetime,timedelta
from django.http import JsonResponse, HttpResponseRedirect
from .SBMercadoPago import *
from .SBUtils import *

from django.db.models import Q

#---------------------------------------------------------
#----------------------CANDY MUEBLE------------------------
#---------------------------------------------------------



def index(request):
	categoria=Categoria.objects.all()
	producto=Producto.objects.filter(destacado=True)
	dic={'categorias':categoria,'productos':producto}
	return render(request,'candymuebles/index.html',dic)

def productos(request):
	print(request.GET)
	pagina = request.GET.get('pagina',1)
	idcat=request.GET.get('categoria','')
	print(idcat)
	if idcat == "":
		productos= Producto.objects.all()	
		category= ""
	else:
		productos= Producto.objects.filter(categoria_idcategoria=idcat)
		category = int(idcat)
		print(category)

	print(pagina)
	row_count = len(productos) 
	p = Paginator(productos, 2)
	pages = p.page(pagina)
	productos = pages.object_list

	categoria= Categoria.objects.all()
	dic={'productos':productos,'categorias':categoria,'pagina':pagina,'row_count':row_count,'startpage':pagina,'pages':pages,'categoria':category}
	return render(request,'candymuebles/productos.html',dic)

def item(request):
	if request.GET:
		idpro=request.GET['idpro']
		producto= Producto.objects.get(idproducto=idpro)
	else:
		return redirect('/')
	categoria= Categoria.objects.all()	
	dic={'producto':producto,'categorias':categoria}
	return render(request,'candymuebles/item.html',dic)

def consultaDisponibilidad(request):
	if request.GET:
		fecha_ini_calend = request.GET.get('fecha_ini_calend','')
		fecha_fin_calend = request.GET.get('fecha_fin_calend','')
		idproduct = request.GET.get('idproduct','')
		cantidad = request.GET.get('cantidad','')
		fecha_ini = request.GET.get('fechaini','')
		fecha_fin = request.GET.get('fechafin','')
		fecha_ini = datetime.strptime(fecha_ini, '%d/%m/%Y').strftime('%Y-%m-%d')
		fecha_fin = datetime.strptime(fecha_fin, '%d/%m/%Y').strftime('%Y-%m-%d')

		rango_fecha = ConsultarRangoFecha(fecha_ini_calend,fecha_fin_calend,idproduct,cantidad,fecha_ini,fecha_fin)
	return JsonResponse(rango_fecha, safe=False)
	
def ConsultarRangoFecha(fecha_ini_calend,fecha_fin_calend,idproduct,cantidad,fecha_ini,fecha_fin):
	detallepedido = PedidoDetalle.objects.filter(Q(fecha_ini__range=(fecha_ini_calend,fecha_fin_calend)) | Q(fecha_fin__range=(fecha_ini_calend,fecha_fin_calend)),producto_idproducto=idproduct)
	product = Producto.objects.filter(idproducto=idproduct)
	rango_fecha = CalculaRangoFecha(fecha_ini_calend,fecha_fin_calend)

	fecha_ini = datetime.strptime(fecha_ini, "%Y-%m-%d").date()
	fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
	for fila in rango_fecha:
		# print(fila[0],fila[1],fila[2],fila[3])
		# print(product[0].stock)
		fila[1] = product[0].stock
		fila[2] = Sumatoria(fila,detallepedido)
		fila[3] = fila[1]-fila[2]
		fila[4] = product[0].nombre
		fila[5] = cantidad
		fila_fecha = datetime.strptime(fila[0], "%Y-%m-%d").date()
		if (fecha_ini <= fila_fecha <= fecha_fin):
			fila[3] = fila[3] - int(cantidad)
		# print(fila[0],fila[1],fila[2],fila[3])

	return rango_fecha

def CalculaRangoFecha(fecha_ini,fecha_fin):
	st=[str(fecha_ini),str(fecha_fin)]
	start=datetime.strptime(st[0],"%Y-%m-%d")
	end=datetime.strptime(st[1],"%Y-%m-%d")
	r = [[(start + timedelta(days=i)).strftime("%Y-%m-%d"),0,0,0,'',0] 
	for i in range(0,(end-start).days+1,1)]
	return r
	
def Sumatoria(fila_fecha,detallepedido):
	Disponible = 0
	fila = fila_fecha[0]
	fila = datetime.strptime(fila, "%Y-%m-%d").date()
	for pedet in detallepedido:
		if (pedet.fecha_ini <= fila <= pedet.fecha_fin):
			Disponible = Disponible + pedet.cantidad
	
	return Disponible

def sobre_nosotros(request):
	categoria= Categoria.objects.all()	
	dic={'categorias':categoria}
	return render(request,'candymuebles/sobre_nosotros.html',dic)

def add_carrito(request):
	if request.POST:
		flagnewcant = request.POST.get('flagnewcant','')
		producto = Producto.objects.get(idproducto=request.POST['idpro'])
		cantidad = request.POST['cantidad']
		fechainicio = request.POST.get('fecha_ini','01/01/1999')
		fechainicio = datetime.strptime(fechainicio, '%d/%m/%Y').strftime('%Y-%m-%d')
		fechafin = request.POST.get('fecha_fin','01/01/1999')
		fechafin = datetime.strptime(fechafin, '%d/%m/%Y').strftime('%Y-%m-%d')
		subtotal = int(cantidad)*producto.precio

		if producto.promocion is True or producto.preventa is True:
			subtotal=int(cantidad)*producto.precio_promocion
		else:
			subtotal=int(cantidad)*producto.precio

		if request.session.get('Carrito', False):
			#get carrito
			id_cart=request.session['Carrito']
			carrito=Carrito.objects.get(idcarrito=id_cart)
			#COMENTADO POR MARCO
			#subtotal=int(cantidad)*producto.precio
			test=Carritohasproductos.objects.filter(carrito_idcarrito=carrito,producto_idproducto=producto)
			
			#print("Actualización")
			#print(test)
			#Crear carrito has producto
			if test:
				cant_old = test[0].subtotal
				if flagnewcant == "1":
					#print("enter test producto")
					#Actualizar CarritoHasProducto
					test[0].cantidad=int(cantidad)
					test[0].subtotal=subtotal
					print(test[0].subtotal)
					#Actualizar Carrito
					#request.session['cantidad']=request.session['cantidad']+1
					carrito.total=(carrito.total+subtotal) - cant_old
					test[0].save()
					carrito.save()
					print("actualizo correctamente")
					dic = {'subtotal': test[0].subtotal ,'total':carrito.total}
					return JsonResponse(dic, safe=False)
				else:
					#print("enter test producto")
					#Actualizar CarritoHasProducto
					test[0].cantidad+=int(cantidad)
					test[0].subtotal+=subtotal
					test[0].save()
					#Actualizar Carrito
					#request.session['cantidad']=request.session['cantidad']+1
					carrito.total=carrito.total+subtotal
					carrito.save()
					url='../item/?idpro='+str(producto.idproducto)
					return redirect(url)
			else:
				
				#Crear carrito has producto
				carrito_has_p=Carritohasproductos(carrito_idcarrito=carrito,cantidad=cantidad,subtotal=subtotal,producto_idproducto=producto,fecha_ini=fechainicio,fecha_fin=fechafin)
				carrito_has_p.save()
				request.session['Cantidad']+=1
				carrito.total=carrito.total+subtotal
				carrito.save()
		else:
			#crear carrito
			print(fechainicio)
			carrito= Carrito()
			carrito.save()
			id_cart=carrito.idcarrito
			request.session['Carrito']=id_cart
			#COMENTADO POR MARCO
			#subtotal=int(cantidad)*producto.precio
			#crear carrito has producto
			carrito_has_p=Carritohasproductos(carrito_idcarrito=carrito,cantidad=cantidad,subtotal=subtotal,producto_idproducto=producto,fecha_ini=fechainicio,fecha_fin=fechafin)
			carrito_has_p.save()
			#Actualizar carrito
			request.session['Cantidad']=1
			carrito.total=subtotal
			carrito.save()


		url='../item/?idpro='+str(producto.idproducto)
		return redirect(url)

def carrito(request):
	categoria= Categoria.objects.all()	
	dic={'categorias':categoria}
	if 'Carrito' in request.session:
		#print("paso")
		productos_en_carrito=Carritohasproductos.objects.filter(carrito_idcarrito=request.session['Carrito'])
		dic['productos_en_carrito']=productos_en_carrito
		dic['carrito']=Carrito.objects.get(idcarrito=request.session['Carrito'])

	return render(request,'candymuebles/carrito.html',dic)

def galeria(request):
	print(request.GET)
	categoria= Categoria.objects.all()	
	galeria= Galeria.objects.all()
	print(galeria)
	dic={'galerias':galeria,'categorias':categoria}
	return render(request,'candymuebles/galeria.html',dic)

def contacto(request):
	print("ENTRO AQUIIIII")
	if request.POST:
		tel = request.POST['phone']
		email = request.POST['email']
		nombre = request.POST['firstname']
		mensaje = request.POST['message']
		template = get_template('candymuebles/email_contacto.html')
		context = {'nombre': nombre, 'telefono': tel, 'email': email, 'mensaje': mensaje}
		print(context)
		contenido = template.render(context)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email,]
		asunto='Contacto a través de la Web Candy Muebles'
		send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)
		url = '/?a=Mensaje%20Enviado#extForm17-o'
	return redirect(url) 

def del_carrito(request):
	eliminar=Carritohasproductos.objects.filter(idcarritohasproductos=int(request.POST['idCarritoeliminar']))
	if eliminar:
		eliminar=Carritohasproductos.objects.get(idcarritohasproductos=int(request.POST['idCarritoeliminar']))
		subtotal=eliminar.subtotal
		carrito=Carrito.objects.get(idcarrito=eliminar.carrito_idcarrito.idcarrito)
		carrito.total=carrito.total-subtotal
		request.session['Cantidad']-=1
		carrito.save()
		eliminar.delete()
		url='../carrito'
	return redirect(url)

def realizar_pedido(request):
	categoria= Categoria.objects.all()
	delivery= Delivery.objects.all()
	tipoevento= TipodeEvento.objects.all()
	form=Formulario_Crear_Nuevo()
	productos_en_carrito=Carritohasproductos.objects.filter(carrito_idcarrito=request.session['Carrito'])
	objAlert = {'flagAlert': False}
	arrayControl=[]
	rpt = True
	for c in productos_en_carrito:
		rangofecha=ConsultarRangoFecha(c.fecha_ini,c.fecha_fin,c.producto_idproducto.idproducto,c.cantidad,str(c.fecha_ini),str(c.fecha_fin))
		if (rangofecha[0][3] < 0):
			rpt = False
			objAlert['flagAlert'] = True
		arrayControl.append({'producto':rangofecha[0][4],'stockDisponible':rangofecha[0][3] + rangofecha[0][5],'status':rpt,'cantidad':rangofecha[0][5]})
	objAlert['listAlert'] = arrayControl

	dic={'objalert':objAlert,'form':form,'categorias':categoria,'deliverys':delivery,'tipoeventos':tipoevento,'BtnRegresar':True,}
	return render(request,'candymuebles/Realizar_pedido.html',dic)

def realizar_pedido2(request):
	if request.POST:
		tipodocumentocli=request.POST['tipodocumentoCli']
		nrodocumento=request.POST['nrodocumento']
		nombre=request.POST['nombre']
		email=request.POST['email']
		telefono=request.POST['telefono']
		direcciondomicilio=request.POST['direcciondomicilio']
		direccionevento=request.POST['direccionevento']
		if 'notas' in request.POST:
			notas=request.POST['notas']
		else: 
			notas=''
		delivery_id=request.POST['delivery']
		delivery=Delivery.objects.get(iddelivery=delivery_id)
		precio_delivery=delivery.precio
		delivery_nombre=delivery.nombre
		tipoevento=request.POST['tipoevento']
		tipevent=TipodeEvento.objects.get(idTipodeEvento=tipoevento)
		id_cart=request.session['Carrito']
		carrito=Carrito.objects.get(idcarrito=id_cart)
		# VALIDACIÓN DEL CODIGO DE DESCUENTO
		desctcodigo=request.POST['desctcodigo']
		Descuent = Descuento.objects.filter(Q(fecha_ini__range=(datetime.today(),datetime.today())) | Q(fecha_fin__range=(datetime.today(),datetime.today())),codigoreferido__iexact=desctcodigo,status=True)

		if len(Descuent) != 0:
			if Descuent[0].Monto < carrito.total:
				carrito_total=carrito.total - round(carrito.total * int(Descuent[0].descuento)/100)
				descuento = round(carrito.total * int(Descuent[0].descuento)/100)
				total_delivery=precio_delivery+carrito_total
				
		else:
			carrito_total=carrito.total
			descuento = 0
			total_delivery=precio_delivery+carrito_total

		productos_en_carrito=Carritohasproductos.objects.filter(carrito_idcarrito=carrito)
		Texto="Productos "+" (carrito id="+str(carrito.idcarrito)+")"+": \n"
		arrayControl=[]
		rpt = True
		for c in productos_en_carrito:
			rangofecha=ConsultarRangoFecha(c.fecha_ini,c.fecha_fin,c.producto_idproducto.idproducto,c.cantidad,str(c.fecha_ini),str(c.fecha_fin))
			# print("rangofecha")
			# print(rangofecha)
			if (rangofecha[0][3] < 0):
				rpt = False
			arrayControl.append({'producto':rangofecha[0][4],'stockDisponible':rangofecha[0][3] + rangofecha[0][5],'status':rpt,'cantidad':rangofecha[0][5]})

		if rpt == True:
			for c in productos_en_carrito:
				cantidad= str(c.cantidad)
				subtotal= str(c.subtotal)
				#talla= str(c.talla)
				producto= str(c.producto_idproducto.nombre)
				#linea=producto+': '+' '+talla+' '+cantidad+' -  $ '+subtotal+'\n'
				linea=producto+': '+' '+cantidad+' -  $ '+subtotal+'\n'
				Texto=Texto+linea

			client = Cliente.objects.filter(nrodocumento=nrodocumento,tipo_documento=tipodocumentocli)
			if (len(client) == 0):
				cli=Cliente(
					 tipo_documento=tipodocumentocli
					,nrodocumento=nrodocumento
					,nombre=nombre
					,email=email
					,estatus=1
				)
				cli.save()
				client = cli
			else:
				client = Cliente.objects.get(nrodocumento=nrodocumento,tipo_documento=tipodocumentocli)

			if (int(client.estatus)==3):
				print("ENTRO AQUIIII")
				objAlertClie = {'flagAlertCliente': True}
				categoria= Categoria.objects.all()		
				delivery=Delivery.objects.all()
				tipoevento= TipodeEvento.objects.all()
				print(str(client.nombre))
				obj = {'objAlertClie':objAlertClie,'NomCli': str(client.nombre),'categorias':categoria,'deliverys':delivery,'tipoeventos':tipoevento}
				return render(request,'candymuebles/Realizar_pedido.html',obj)

			compra=Pedido(
					 nombre=nombre
					,email=email
					,telefono=telefono
					,direccion_domicilio=direcciondomicilio
					,direccion_evento=direccionevento
					,notas=notas
					,pedido=Texto
					,delivery_iddelivery=delivery
					,total=carrito_total
					,total_delivery=total_delivery
					,cliente_idcliente=client
					,Tipoevento_idTipodeEvento=tipevent
				)
			compra.save()

			for c in productos_en_carrito:
				pedidodet=PedidoDetalle(
					pedido_idpedido = compra
					,producto_idproducto = c.producto_idproducto
					,cantidad = c.cantidad
					,fecha_ini = c.fecha_ini
					,fecha_fin = c.fecha_fin
					,status = "C"
				)
				pedidodet.save()
			
			EnviarCorreo_Compra('candymuebles/email_compra.html',compra,'galezmark@gmail.com')
			EnviarCorreo_Compra('candymuebles/email_cliente.html',compra,email)

			MercadoPagoResult  = GeneraBotonPago(compra.idpedido,"Compra en: Candy Muebles",compra.total_delivery)

			total=carrito_total
			#---
			categoria= Categoria.objects.all()
			#---
			obj = {'nombre':'Candy Muebles','carrito_has_p':productos_en_carrito,'compra':compra,'total':total,'categorias':categoria,'descuento':descuento,'MercadoPagoResult':MercadoPagoResult}
			request.session.flush()
			return render(request,'candymuebles/Realizar_pedido_2.html',obj)
		else:
			objAlert = {'flagAlert': False}
			categoria= Categoria.objects.all()		
			delivery=Delivery.objects.all()
			tipoevento= TipodeEvento.objects.all()
			objAlert['flagAlert'] = True
			objAlert['listAlert'] = arrayControl
			obj = {'objalert':objAlert,'categorias':categoria,'deliverys':delivery,'BtnRegresar':True,'tipoeventos':tipoevento}
			return render(request,'candymuebles/Realizar_pedido.html',obj)
	else:
		return redirect("../")

def busquedacliente(request):
	if request.method == 'POST':
		print(request)
		nrodocumento=request.POST['nrodocumento']
		dniruc=request.POST['tipodoc']
		#print(type(dniruc))
		cliente=Cliente.objects.filter(nrodocumento=int(nrodocumento),tipo_documento=int(dniruc))
		print(len(cliente))
		namecli = ""
		emailcli = ""

		if len(cliente) == 1:
			namecli = cliente[0].nombre
			emailcli = cliente[0].email

		dic = {'nrodocumento':nrodocumento,'namecli':namecli,'emailcli':emailcli}
	return JsonResponse(dic, safe=False)

def ValidateCodigoDescuento(request):
	if request.method == 'GET':
		id_cart=request.session['Carrito']
		carrito=Carrito.objects.get(idcarrito=id_cart)
		desctcodigo=request.GET['desctcodigo']
		Descuent = Descuento.objects.filter(Q(fecha_ini__range=(datetime.today(),datetime.today())) | Q(fecha_fin__range=(datetime.today(),datetime.today())),codigoreferido__iexact=desctcodigo,status=True)
		descuento = 0

		if len(Descuent) == 1 and Descuent[0].Monto < carrito.total:
			descuento = Descuent[0].descuento

		dic = {'descuento':descuento}
	return JsonResponse(dic, safe=False)