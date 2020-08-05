import io
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper
from django.shortcuts import render
from django.core.files import File

# Create your views here.
def home(request):
    return render(request, "app/home.html")