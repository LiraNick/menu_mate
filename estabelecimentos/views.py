from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .models import Mesa



def index(request):

    mesas = Mesa.objects.all()

    context = {'mesas': mesas}

    return render(request,'principal.html', context)