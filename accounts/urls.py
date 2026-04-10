from django.urls import path
from .views import SignupView, profile, edit_profile

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("perfil/", profile, name="perfil"),
    path("editar/", edit_profile, name="editar_perfil"),
]