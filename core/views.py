from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

#this view handels the home page
def home(request):
    articles = Article.objects.published

    context = {'articles': articles, 'site_title': 'HOME'}

    return render(request, 'core/home.html', context=context)

#this view handels content of each post
def post(request ,slug):
    article = get_object_or_404(Article.objects.published(), slug=slug,)
    context = {'article': article.context, 'site_title': article.title, 'image': article.image,
               'create_date': article.create_date,}
    return render(request, 'core/index.html', context=context)
