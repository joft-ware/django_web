from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from accountapp.models import hw


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        news = hw()
        news.text = temp
        news.save()

        return render(request, 'accountapp/hello.html', context={'hello_world_output':news})
    else:
        return render(request, 'accountapp/hello.html', context={'text':'GET METHOD!!!'})