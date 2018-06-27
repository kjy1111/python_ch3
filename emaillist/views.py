from django.shortcuts import render
from emaillist.models import Emaillist
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    emaillist_list = Emaillist.objects.all().order_by('-id')
    data = {'emaillist_list': emaillist_list}
    return render(request, 'index.html', data)


def form(request):
    return render(request, 'form.html')


def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    return HttpResponseRedirect('/emaillist')