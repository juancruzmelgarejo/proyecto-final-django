from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviar/<int:user_id>/', views.enviar_mensaje, name='enviar'),
]