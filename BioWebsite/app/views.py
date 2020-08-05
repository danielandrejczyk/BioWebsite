import io
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.shortcuts import render, get_object_or_404
from django.core.files import File
from django.template import loader
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.order_by('-publish_date')[:1]
    context = {'articles': articles}
    return render(request, 'app/ArticleList.html', context)

def content_view(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'app/ArticleView.html', {'article': article})