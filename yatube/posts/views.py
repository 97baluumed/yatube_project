from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    group_text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'gr_text': group_text,
    }
    return render(request, template, context)
