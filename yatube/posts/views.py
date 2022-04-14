from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html_content = '<html><head><title>yatube - соц. сеть для блогеров</title></head><body>'
    html_content += '<h1>Главная страница</h1>'
    html_content += '</body></html>'    
    return HttpResponse(html_content) 

def group_posts(request):
    return HttpResponse('Посты, отфильтрованные по группам')