import mercadopago

# def Add(a,b):
#    return a+b 
# def subtract(a,b):
#   return a-b

def GeneraBotonPago(idpedido,nombreproducto,total):
   mp = mercadopago.MP('2545425583027464','Yp3gjXaD5YRwG6V7rLXRLSBA7jYIxV9l')    
   preference = {
      "items": [
         	{	
				"id": 'ID-CANDY-MUEBLES-'+str(idpedido),
				"title": nombreproducto,
				"currency_id": "CLP",
				"description": "Compra a Candy Muebles",
				"quantity": 1,
				"unit_price": total
			}
		]
      ,"back_urls": {
		   "success": "localhost:8000/compra_exito/",
			"failure": "localhost:8000/compra_fallo/",
			"pending": "localhost:8000/compra_proceso/"
			}
      ,"external_reference": idpedido
   }
   preferenceResult = mp.create_preference(preference)   
   return preferenceResult