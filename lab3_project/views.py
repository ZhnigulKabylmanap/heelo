from django.shortcuts import render,get_object_or_404
from.models import *
def show_post(request,post_id):
    post = get_object_or_404(Posts, pk=post_id)
    context = {'post': post}
    return render(request, 'lab3_project/p1.html', context=context)
def show_slug(request,post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'post': post}
    return render(request, 'lab3_project/p1.html', context=context)

def p2(request):
    return render(request,'lab3_project/p2.html')

def p3(request):
    return render(request,'lab3_project/p3.html')


