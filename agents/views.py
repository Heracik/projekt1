from .models import Agent
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agents/agent_list.html', {'agents': agents})

@login_required
def agent_detail(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    return render(request, 'agents/agent_detail.html', {'agent': agent})

def register(request):
    message = " "
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")  

        if form.is_valid():
            user = form.save()
            login(request, user)

            # Odoslanie e-mailu
            subject = "Vitajte v našej stránke!"
            message = f"Ahoj {username},\n\nĎakujeme za registráciu. "
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect("agents:agent_list")  # Zmena z polls:index na rentals:index
        else:
            message = "Registrácia zlyhala. Skontrolujte chyby nižšie."
    else:
        form = CustomUserCreationForm(request.POST)

    return render(request, "accounts/register.html", {"form": form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f'User logged in: {user.username}')
            return redirect("agents:agent_list")  # Zmena z polls:index na rentals:index
        else:
            print(f"Neplatné prihlasovacie údaje")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})



@login_required
def logout_view(request):
    logout(request)
    #messages.info(request, "Úspešne ste sa odhlásili.")
    return redirect("agents:agent_list")

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]