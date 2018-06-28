from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/index.html', context)


def delete(request):
    guest_id = request.POST['id']
    guest_pw = request.POST['password']
    Guestbook.objects.filter(id=guest_id).filter(password=guest_pw).delete()
    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    guest_id = request.GET['id']
    context = {'guest_id': guest_id}
    return render(request, 'guestbook/deleteform.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')