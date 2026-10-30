from django.shortcuts import render
from .forms import ArizaModelFoem
from django.http import HttpResponse
from .models import ariza, User
from django.contrib.auth import get_user
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def add_ariza(request):
    if request.method == 'POST':
        form = ArizaModelFoem(request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('ariza')
    else:
        form = ArizaModelFoem(user=request.user)

    return render(request, 'ariza.html', {'form': form})






                        