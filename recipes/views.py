# from http.client import HTTPResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Hedward Cordeiro',
        'foco': ' voce vai superar e ser melhor, muito melhor.'
        'github' 'link pro github'
    })
