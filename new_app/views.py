
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout



from django.contrib.auth.decorators import login_required 



from .forms import authentificatemodelform, loginmodelform
from .models import User



def register_view(request):
    if request.method == 'POST':
        form = authentificatemodelform(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
            
    else:
        form = authentificatemodelform()

    return render(request, 'aut.html', {'forms': form})


def login_view(request):
    if request.method == 'POST':
        form = loginmodelform(
            request=request,
            data=request.POST
        )

        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = loginmodelform()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('home')


@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')
