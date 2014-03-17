from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponse
from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.template.context import RequestContext

def sobre(request):
    html='<html><body>Proyecto de Ejemplo en MDW</body></html>'
    return HttpResponse(html)

def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html',{'recetas':recetas})

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html', {'usuarios':usuarios,
                                                'recetas':recetas})
    
def listaRecetas(request):
    recetas = Receta.objects.all()
    return render_to_response('recetas.html', {'datos':recetas},
                              context_instance = RequestContext(request))
    
def detalleReceta(request, idReceta):
    dato = get_object_or_404(Receta, pk=idReceta)
    comentarios = Comentario.objects.filter(receta=dato)
    return render_to_response('receta.html', {'receta':dato,
                                              'comentarios':comentarios},
                              context_instance=RequestContext(request))