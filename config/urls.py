from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # App principal
    path('', include('mi_app.urls')),

    # Accounts
    path('accounts/', include('accounts.urls')),

    # Mensajes 👇
    path('mensajes/', include('mensajes.urls')),

    # Auth
    path('login/', auth_views.LoginView.as_view(
        template_name='mi_app/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'
    ), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)