from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_html(request):
    return render(request, 'portfolio/index.html')zz