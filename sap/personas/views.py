from django.forms import modelform_factory
from django.shortcuts import render, redirect

from personas.forms import PersonaForm
from personas.models import Persona


# Create your views here.
def detallePersona(request,id):
    persona = Persona.objects.get(pk=id)
    #persona = get_object_or_484(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona':persona})

#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return  redirect('inicio') #index or inicio
        #else:
        #    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(request,id):
    persona = Persona.objects.get(pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance= persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return  redirect('inicio') #index or inicio
        #else:
        #    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
    else:

        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

def eliminarPersona(request,id):
    persona = Persona.objects.get(pk=id)
    if persona:
        persona.delete()
        return  redirect('inicio')
