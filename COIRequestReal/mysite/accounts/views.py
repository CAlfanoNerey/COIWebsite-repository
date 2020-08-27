from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RequesterForm
from django.contrib.auth.models import User


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required()
def dashboardView(request):
    return render(request, 'dashboard.html')

def logoutview(request):
    return render(request, 'registration/logout.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def requesterView(request):
    # context= {}
    # form = RequesterForm(request.POST)
    # context['form'] = form

    args = {'user': request.user}

    if request.method == "POST":

        context = {}
        form = RequesterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RequesterForm()
    return render(request, 'requester.html', {'form': form},)


def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)
