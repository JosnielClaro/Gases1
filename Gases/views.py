from django.shortcuts import render
from Gases.figura import triangulo_1,triangulo_4,triangulo_5,an_triangulo_1,porcient,an_triangulo_4,an_triangulo_5
from triangulo_app.models import transformador
from django.shortcuts import redirect
#from plotly.offline import plot
# Create your views here.
def homehtml(request):
    lista = transformador.objects.all()
    fig1 = triangulo_4 ([0], [0], [0],'')
    fig2 = triangulo_5 ([0], [0], [0],'')
    name = []
    ch4 = []
    c2h2= []
    c2h4= []
    h2 = []
    c2h6 = []

    for c in lista:
        name.append(c.nombre)
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

    ch4a = porcient(ch4,c2h2,c2h4)
    c2h2a = porcient(c2h2,ch4,c2h4)
    c2h4a = porcient(c2h4,ch4,c2h2)
    ch4b = []
    h2b = []
    c2h6b =[]
    nameb = []
    id4 = []
    id5 = []

    fig = triangulo_1 (ch4a, c2h2a, c2h4a, name)
    for a,b,c,d,e,f,g,h in zip(ch4a, c2h2a, c2h4a, name, ch4, h2, c2h6, lista):
        er = h
        er.t1fallas = an_triangulo_1 (a, b, c)
        er.t4fallas = ''
        er.t5fallas = ''
        er.save()
        if an_triangulo_1 (a, b, c) == 'PD' or (
            an_triangulo_1 (a, b, c) == 'T1') or (
                an_triangulo_1 (a, b, c) == 'T2'):
                ch4b.append(e)
                h2b.append(f)
                c2h6b.append(g)
                nameb.append(d)
                id4.append(h)                

    ch4c = porcient(ch4b,h2b,c2h6b)
    h2c = porcient(h2b,ch4b,c2h6b)
    c2h6c = porcient(c2h6b,ch4b,h2b)
    
    for a,b,c,d in zip(h2c, c2h6c, ch4c, id4):
        er4 = d
        er4.t4fallas = an_triangulo_4 (a, b, c)
        er4.save()
        

    ch4d = []
    c2h6d = []
    c2h4d =[]
    named = []

    fig1 = triangulo_4 (h2c, c2h6c, ch4c, nameb)

    for a,b,c,d,e,f,g,h in zip(ch4a, c2h2a, c2h4a, name, ch4, c2h6, c2h4, lista):
        if an_triangulo_1 (a, b, c) == 'T2' or(
            an_triangulo_1 (a, b, c) == 'T3'):
            ch4d.append(e)
            c2h6d.append(f)
            c2h4d.append(g)
            named.append(d)
            id5.append(h)

    ch4e = porcient(ch4d,c2h4d,c2h6d)
    c2h6e = porcient(c2h6d,ch4d,c2h4d)
    c2h4e = porcient(c2h4d,c2h6d,ch4d)
    
    for a,b,c,d in zip(ch4e, c2h6e, c2h4e, id5):
        er5 = d
        er5.t5fallas = an_triangulo_5 (a, b, c)
        er5.save()
            
    fig2 = triangulo_5 (ch4e, c2h6e, c2h4e, named)
    figu = fig.to_html()
    figu1 = fig1.to_html()
    figu2 = fig2.to_html()
    contexto = {'transformadores':lista, 'figura':figu, 'figura1':figu1, 'figura2':figu2}
    return render(request, 'homeplantilla.html', contexto)

def eliminartransf(request, id):
    transf = transformador.objects.get(id=id)
    transf.delete()
    return redirect('/')

def fallas(request):  
    lista = transformador.objects.all()
    contexto = {'transformadores':lista}
    return render(request, 'transfallas.html', contexto)

def triangulo1(request, id):
    transf = transformador.objects.get(id=id)
    ch4 = [float(transf.CH4ppm)]
    c2h2 = [float(transf.C2H2ppm)]
    c2h4 = [float(transf.C2H4ppm)]
    fig = triangulo_1 (ch4, c2h2, c2h4, transf.nombre)
    figu = fig.to_html()
    contexto = {'figura':figu}
    return render(request, 'figura.html', contexto)
def triangulo4(request, id):
    transf = transformador.objects.get(id=id)
    h2 = [float(transf.H2ppm)]
    c2h6 = [float(transf.C2H6ppm)]
    ch4 = [float(transf.CH4ppm)]
    fig = triangulo_4 (h2, c2h6, ch4, transf.nombre)
    figu = fig.to_html()
    contexto = {'figura':figu}
    return render(request, 'figura.html', contexto)
def triangulo5(request, id):
    transf = transformador.objects.get(id=id)
    ch4 = [float(transf.CH4ppm)]
    c2h6 = [float(transf.C2H6ppm)]
    c2h4 = [float(transf.C2H4ppm)]
    fig = triangulo_5 (ch4, c2h6, c2h4, transf.nombre)
    figu = fig.to_html()
    contexto = {'figura':figu}
    return render(request, 'figura.html', contexto)
    
    