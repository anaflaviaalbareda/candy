from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings

def EnviarCorreo_Compra(template,compra,email):
   template = get_template(template)
   context = { 'compra': compra}
   contenido = template.render(context)
   email_from = settings.EMAIL_HOST_USER
   recipient_list = [email,]
   asunto='Pedido a través de Tienda Online'
   send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)
   return True

