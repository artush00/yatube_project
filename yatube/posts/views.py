from django.shortcuts import render
from django.http import HttpResponse



def group_posts(request, slug):
    return HttpResponse(f'Список {slug}')
# Create your views here.

def index(request):
    template = 'posts/index.html'
    return render(request, template) 
