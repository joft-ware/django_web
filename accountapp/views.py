from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import hw

has_ownership = [account_ownership_required, login_required]

@login_required
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
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name='target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name='target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name='target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'