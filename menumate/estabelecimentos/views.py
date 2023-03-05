from django.shortcuts import render
from . models import Mesa


# Index irá exibir a página contendo as mesas
def index(request):
    
    mesas = Mesa.objects.all()
    
    context = {
        'mesas': mesas
    }
    
    return render(request, 'index.html', context)


def login(request):
    
    return render(request, 'login.html')

