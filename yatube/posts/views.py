from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    title = "Yatube"
    text = "Это главная страница проекта Yatube"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context) 

def group_posts(request, slug):
    template = 'posts/group_list.html'
    group_text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'gr_text': group_text,
    }
    return render(request, template, context)
