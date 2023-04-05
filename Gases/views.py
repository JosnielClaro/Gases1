from django.shortcuts import render
from Gases.figura import triangulo_1,triangulo_4,triangulo_5,an_triangulo_1,porcient,an_triangulo_4,an_triangulo_5,porcient1
from triangulo_app.models import transformador
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView
from triangulo_app.serializer import gasserializer
# from plotly.offline import plot
# import plotly.graph_objects as go
# Create your views here.
def homehtml(request):
    lista = transformador.objects.all()
    fig1 = triangulo_4 ([0], [0], [0],'','')
    fig2 = triangulo_5 ([0], [0], [0],'','')
    name = []
    fecha = []
    ch4 = []
    c2h2= []
    c2h4= []
    h2 = []
    c2h6 = []

    for c in lista:
        name.append(c.nombre.nombre)
        try:
            ch4.append(float(c.CH4ppm))
        except ValueError:
            pass
        try:
            c2h2.append(float(c.C2H2ppm))
        except ValueError:
            pass
        try:
            c2h4.append(float(c.C2H4ppm))
        except ValueError:
            pass
        try:
            h2.append(float(c.H2ppm))
        except ValueError:
            pass
        try:
            c2h6.append(float(c.C2H6ppm))
        except ValueError:
            pass
        try:
            fecha.append(str(c.fecha.strftime("%d/%m/%Y")))
        except ValueError:
            pass
        
    print(name, fecha)
    ch4a = porcient(ch4,c2h2,c2h4)
    c2h2a = porcient(c2h2,ch4,c2h4)
    c2h4a = porcient(c2h4,ch4,c2h2)
    ch4b = []
    h2b = []
    c2h6b =[]
    nameb = []
    fechab = []
    id4 = []
    id5 = []

    fig = triangulo_1 (ch4a, c2h2a, c2h4a, name, fecha)
    for a,b,c,d,e,f,g,h,i in zip(ch4a, c2h2a, c2h4a, name, ch4, h2, c2h6, lista, fecha):
        er = h
        if an_triangulo_1 (a, b, c) == 'PD' or (
            an_triangulo_1 (a, b, c) == 'T1') or (
                an_triangulo_1 (a, b, c) == 'T2'):
                ch4b.append(e)
                h2b.append(f)
                c2h6b.append(g)
                nameb.append(d)
                fechab.append(i)
                id4.append(h)                

    ch4c = porcient(ch4b,h2b,c2h6b)
    h2c = porcient(h2b,ch4b,c2h6b)
    c2h6c = porcient(c2h6b,ch4b,h2b)

    ch4d = []
    c2h6d = []
    c2h4d =[]
    named = []
    fechad = []

    fig1 = triangulo_4 (h2c, c2h6c, ch4c, nameb, fechab)

    for a,b,c,d,e,f,g,h,i in zip(ch4a, c2h2a, c2h4a, name, ch4, c2h6, c2h4, lista, fecha):
        if an_triangulo_1 (a, b, c) == 'T2' or(
            an_triangulo_1 (a, b, c) == 'T3'):
            ch4d.append(e)
            c2h6d.append(f)
            c2h4d.append(g)
            named.append(d)
            fechad.append(i)
            id5.append(h)

    ch4e = porcient(ch4d,c2h4d,c2h6d)
    c2h6e = porcient(c2h6d,ch4d,c2h4d)
    c2h4e = porcient(c2h4d,c2h6d,ch4d)
                
    fig2 = triangulo_5 (ch4e, c2h6e, c2h4e, named, fechad)
    figu = fig.to_html()
    figu1 = fig1.to_html()
    figu2 = fig2.to_html()
    contexto = {'transformadores':lista, 'figura':figu, 'figura1':figu1, 'figura2':figu2}
    return render(request, 'homeplantilla.html', contexto)

def fallas(request):  
    lista = transformador.objects.all()
    contexto = {'transformadores':lista}
    return render(request, 'transfallas.html', contexto)

def triangulo1(request, id):
    transf = transformador.objects.get(id=id)
    ch4 = [float(transf.CH4ppm)]
    c2h2 = [float(transf.C2H2ppm)]
    c2h4 = [float(transf.C2H4ppm)]
    fig = triangulo_1 (ch4, c2h2, c2h4, [transf.nombre.nombre], [str(transf.fecha.strftime("%d/%m/%Y"))])
    figu = fig.to_html()
    contexto = {'figura':figu}
    return render(request, 'figura.html', contexto)
def triangulo4(request, id):
    transf = transformador.objects.get(id=id)
    h2 = [float(transf.H2ppm)]
    c2h6 = [float(transf.C2H6ppm)]
    ch4 = [float(transf.CH4ppm)]
    fig = triangulo_4 (h2, c2h6, ch4, [transf.nombre.nombre], [str(transf.fecha.strftime("%d/%m/%Y"))])
    figu = fig.to_html()
    contexto = {'figura':figu}
    return render(request, 'figura.html', contexto)
def triangulo5(request, id):
    transf = transformador.objects.get(id=id)
    ch4 = [float(transf.CH4ppm)]
    c2h6 = [float(transf.C2H6ppm)]
    c2h4 = [float(transf.C2H4ppm)]
    fig = triangulo_5 (ch4, c2h6, c2h4, [transf.nombre.nombre], [str(transf.fecha.strftime("%d/%m/%Y"))])
    figu = fig.to_html()
    contexto = {'figura':figu}
    return render(request, 'figura.html', contexto)

class TransfList(ListAPIView):
    serializer_class = gasserializer
    
    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        fecha = self.request.query_params.get('fecha', '')
        
        return transformador.objects.filter(
        fecha__contains=fecha, nombre=kword
        )
class TransfList1(ListAPIView):
    serializer_class = gasserializer
    
    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return transformador.objects.filter(
        nombre=kword
        )

# def agregartransf(request):
#     nombre = request.POST['Nombre']
#     CH4ppm = float(request.POST['CH4ppm'])
#     C2H4ppm = float(request.POST['C2H4ppm'])
#     C2H6ppm = float(request.POST['C2H6ppm'])
#     H2ppm = float(request.POST['H2ppm'])
#     C2H2ppm = float(request.POST['C2H2ppm'])
#     t4fallas = ''
#     t5fallas = ''
#     ch4a = porcient1(CH4ppm,C2H2ppm,C2H4ppm)
#     c2h2a = porcient1(C2H2ppm,CH4ppm,C2H4ppm)
#     c2h4a = porcient1(C2H4ppm,CH4ppm,C2H2ppm)
#     t1fallas = an_triangulo_1 (ch4a, c2h2a, c2h4a)
#     if t1fallas == 'PD' or (
#             t1fallas == 'T1') or (
#                 t1fallas == 'T2'):    
#                     ch4b = porcient1(CH4ppm,H2ppm,C2H6ppm)
#                     h2b = porcient1(H2ppm,CH4ppm,C2H6ppm)
#                     c2h6b = porcient1(C2H6ppm,CH4ppm,H2ppm)
#                     t4fallas = an_triangulo_4 (ch4b, h2b, c2h6b)
#     if t1fallas == 'T2' or(
#             t1fallas == 'T3'):                
#                 ch4c = porcient1(CH4ppm,C2H4ppm,C2H6ppm)
#                 c2h6c = porcient1(C2H6ppm,CH4ppm,C2H4ppm)
#                 c2h4c = porcient1(C2H4ppm,C2H6ppm,CH4ppm)
#                 t5fallas = an_triangulo_5 (ch4c, c2h6c, c2h4c)
    
#     transformador.objects.create(nombre=nombre, CH4ppm=CH4ppm, C2H4ppm=C2H4ppm, t1fallas=t1fallas, t4fallas=t4fallas,
#                                 t5fallas=t5fallas, C2H6ppm=C2H6ppm, H2ppm=H2ppm, C2H2ppm=C2H2ppm)
#     return redirect('/agregar')
    
# def agregar(request):
#     return render(request, 'agregar.html')

# def editar (request, id):
    # transf = transformador.objects.get(id=id)
    # data = {
    #     'transf': transf
    # }
    # return render(request, 'editar.html', data)

# def editartransf (request):
#     id = int(request.POST['id'])
#     nombre = request.POST['Nombre']
#     CH4ppm = float(request.POST['CH4ppm'])
#     C2H4ppm = float(request.POST['C2H4ppm'])
#     C2H6ppm = float(request.POST['C2H6ppm'])
#     H2ppm = float(request.POST['H2ppm'])
#     C2H2ppm = float(request.POST['C2H2ppm'])
    
#     transf = transformador.objects.get(id=id)
#     transf.nombre = nombre
#     transf.CH4ppm = CH4ppm
#     transf.C2H4ppm = C2H4ppm
#     transf.C2H6ppm = C2H6ppm
#     transf.H2ppm = H2ppm
#     transf.C2H2ppm = C2H2ppm
#     transf.save()
#     return redirect('/agregar')
    

    