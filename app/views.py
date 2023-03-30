from django.shortcuts import render
from .forms import Alumno

# Create your views here.


def registrar(request):
    if request.method == "POST":
        # crear objeto de la clase alumno
        form = Alumno(request.POST)
        if form.is_valid():
            # asignar valores a la variables
            codigo = form.cleaned_data["codigo"]
            nombre = form.cleaned_data["nombre"]
            curso = form.cleaned_data["curso"]
            parcial = form.cleaned_data["parcial"]
            final = form.cleaned_data["final"]
            practica = form.cleaned_data["practica"]
            # procesar
            promedio = (parcial+practica+2*final)/4
            if promedio >= 14:
                estado = "Aprobado"
            elif promedio >= 10 and promedio < 14:
                estado = "Sustitutorio"
            else:
                estado = "Desaprobado"
            contexto = {"codigo": codigo, "nombre": nombre, "curso": curso,
                        "parcial": parcial, "final": final,"practica":practica, "promedio": promedio, "estado": estado}
            return render(request, "app/boleta.html", contexto)
    else:
        # crear objeto de la clase Alumno
        form = Alumno()
    contexto = {"form": form}
    return render(request, "app/registrar.html", contexto)
