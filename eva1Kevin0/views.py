from django.shortcuts import render

# Create your views here.

def renderIndex(request):
    data = {"devil":"static/imagenes/devil.webp", "resident":"static/imagenes/resident.webp", "elden":"static/imagenes/elden.webp"}
    return render(request, "eva1Kevin0/index.html", data)

def renderDevil(request):
    data = {"Nombre":"Devil My Cry V", "Juego":"static/imagenes/devil.webp", "desc":"Quinto juego de la saga", "valo":"8.3"}
    return render(request, "eva1Kevin0/pagina.html", data)

def renderResident(request):
    data = {"Nombre":"Resident evil 4", "Juego":"static/imagenes/resident.webp", "desc":"Cuarto juego de la saga", "valo":"9"}
    return render(request, "eva1Kevin0/pagina.html", data)

def renderElden(request):
    data = {"Nombre":"Elden Ring", "Juego":"static/imagenes/elden.webp", "desc":"Juego estilo souls", "valo":"9.6"}
    return render(request, "eva1Kevin0/pagina.html", data)
