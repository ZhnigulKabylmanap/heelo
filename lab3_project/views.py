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

from django.core.mail import EmailMessage
def send_message(request):
    email=EmailMessage("Zhainigul","Here is a picture for you","200103272@stu.sdu.edu.kz",['200103272@stu.sdu.edu.kz'],headers={'Message-ID':'foo'})
    email.attach_file('C:/WebFinal/picture.jpg')
    email.send(fail_silently=False)
    return render(request,'lab3_project/mail.html')


