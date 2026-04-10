from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile


class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mi_app:inicio")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# 🔥 PERFIL
@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'accounts/perfil.html', {'profile': profile})


# 🔥 EDITAR PERFIL
@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:perfil')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'form': form})