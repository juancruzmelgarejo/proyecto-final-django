from django.urls import path
from . import views
from .views import PostListView, PostDetailView

app_name = 'mi_app'

urlpatterns = [
    path('', views.home, name='home'),

    path('pages/', views.inicio, name='inicio'),
    path('pages/<int:id>/', views.detalle_post, name='detalle_post'),

    path('pages/crear/', views.crear_post, name='crear_post'),
    path('pages/editar/<int:id>/', views.editar_post, name='editar_post'),
    path('pages/eliminar/<int:id>/', views.eliminar_post, name='eliminar_post'),

    path('buscar/', views.buscar, name='buscar'),

    path('about/', views.about, name='about'),
    
    path('pages/', PostListView.as_view(), name='inicio'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='detalle_post'),
]