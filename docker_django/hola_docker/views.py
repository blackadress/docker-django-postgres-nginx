from django.shortcuts import render

# Create your views here.
def hola(request):
    context = {
        "hola": "Hola desde Django-docker"
    }
    return render(request, 'hola.html', context)