from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/index.html', context)


# def delete(request):
#     Guestbook.objects.filter(id=request.id).filter(password=request.GET['password']).delete()
#     return render(request, 'guestbook/deleteform.html')


def deleteform(request):
    Guestbook.objects.filter(id=request.GET['id']).filter(password='password').delete()
    return render(request, 'guestbook/deleteform.html')
    # return render(request, 'guestbook/deleteform.html')


def add(request):
    guestbook = Guestbook()
    guestbook.id = request.POST['id']
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')