from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def homehtml(request):
    plantillaex = open('C:\django-rest\Gases\Gases\Plantillas\homeplantilla.html')
    template = Template(plantillaex.read())
    plantillaex.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)