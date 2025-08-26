from django.http import HttpResponse
from django.template import Template, context
from django.template import loader

def home(request): # pagina Home
    hometemp = loader.get_template('home.html')
    documento01 = hometemp.render()
    return HttpResponse(documento01)

def contacto(request): # pagina contacto
    contactotemp = loader.get_template('contacto.html')
    documento02 = contactotemp.render()
    return HttpResponse(documento02)

def servicios(request): # pagina servicios
    serviciostemp = loader.get_template('servicios.html')
    documento03 = serviciostemp.render()
    return HttpResponse(documento03)

# Create your views here.
