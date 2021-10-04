from django.conf import settings
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import Task


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import FormView

from django.contrib.auth.views import LogoutView, LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'account/home-page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'account/task-detail.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    template_name = 'account/task-create.html'
    success_url = reverse_lazy('account:tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'account/task-create.html'
    success_url = reverse_lazy('account:tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('account:tasks')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:home')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


def login_Page(request):
    if request.method == "POST":
        cd = request.POST
        username = cd['username']
        password = cd["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('account:tasks')
            else:
                messages.error(request, "User is not active")
        else:
            messages.error(request, "Username Or password is Incorrect")

    return render(request, 'account/login.html')


class logoutPage(LogoutView):
    next_page = reverse_lazy('account:login')


class registerPage(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('account:tasks')
        return super().get(*args, **kwargs)


class loginPage(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account:tasks')

    def form_invalid(self, form):
        messages.error(self.request, 'Username Or password is Incorrect')
        return super().form_invalid(self)