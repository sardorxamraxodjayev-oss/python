from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from new_app.models import ariza
from django.shortcuts import render, redirect



@login_required

def mening_arizalarim(request):

    if request.user.is_authentificated:

        user = request.user
        arizalar = ariza.objects.filter(user = user)
        return render(request, 'arizalar.html',{'arizalar': arizalar})

    else:
        return redirect('')