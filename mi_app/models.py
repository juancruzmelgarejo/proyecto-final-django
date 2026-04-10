from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo