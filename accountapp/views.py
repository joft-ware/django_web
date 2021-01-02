from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import hw


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')
        news = hw()
        news.text = temp
        news.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hwlist = hw.objects.all()
        return render(request, 'accountapp/hello.html', context={'hwlist': hwlist})


class AccountCreateView(CreateView):
    model: User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'