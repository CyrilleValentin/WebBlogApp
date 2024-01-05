from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from auth_app.models import User 
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
       # Vérifier que le nom d'utilisateur n'est pas déjà utilisé
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà utiliser.')
            return redirect('/login/')  # Remplacez 'registration/register.html' par votre propre modèle de formulaire d'inscription
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email déjà utilisé.')
            return redirect('/login/')
        
          # Créer un nouvel utilisateur avec un mot de passe crypté
        user = User(username=username, email=email)
        user.set_password(password)  # Crypter le mot de passe
        user.save()
        
        messages.success(request, 'Compte creer avec succes.')
        return redirect('/login/')  # Remplacez 'registration/register.html' par votre propre modèle de formulaire d'inscription
        
        
    return render(request, 'register.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'email ou mot de passe incorrect.')
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

def logout1(request):
    logout(request)
    return redirect('login')