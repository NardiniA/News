from django.shortcuts import render
from .models import Article
from .utils import validateID, validateStr

from django.http import HttpResponse

def home(request):
    return render(request, 'news/index.html')

def papers(request):
    return HttpResponse("This is the newspapers page")

def news(request):
    articles = Article.objects.all()
    return render(request, 'news/news.html', {'articles':articles})

def searchArticles(request):
    q = request.GET.get('q')
    if validateStr(q):
        res = Article.objects.filter(title__contains=q)
        return render(request, 'news/search.html', {'res':res})
    else:
        return HttpResponse("Invalid URL")

def article(request, art):
    if validateID(art):
        if Article.objects.filter(pk=art).exists() == 1:
            a = Article.objects.get(pk=art)
            return HttpResponse(a)
        else:
            return HttpResponse("Does not exist")
    else:
        return HttpResponse("Invalid URL")

def contact(request):
    return HttpResponse("This is the contact page")