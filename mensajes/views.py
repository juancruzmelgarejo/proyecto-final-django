from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje

@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha')
    return render(request, 'mensajes/inbox.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request, user_id):
    destinatario = User.objects.get(id=user_id)

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        Mensaje.objects.create(
            remitente=request.user,
            destinatario=destinatario,
            contenido=contenido
        )
        return redirect('mensajes:inbox')

    return render(request, 'mensajes/enviar.html', {'destinatario': destinatario})