from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView

from .forms import RequesterForm, RecipientForm, RegistrationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipient, Requester, User

from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required()
def dashboardView(request):
    return render(request, 'dashboard.html')


def logoutview(request):
    return render(request, 'registration/logged_out.html')


def registerView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            return redirect('login_url')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required()
def requesterView(request):
    # context= {}
    # form = RequesterForm(request.POST)
    # context['form'] = form

    args = {'user': request.user}

    if request.method == "POST":

        context = {}
        form = RequesterForm(request.POST)
        form.instance.user = request.user
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RequesterForm()
    return render(request, 'requester.html', {'form': form}, )


# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'profile.html', args)

class view_profile(generic.DetailView):
    model = Requester
    template_name = 'profile.html'


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')

    else:
        form = UserChangeForm(instance=request.user)
        args= {'form': form}
        return render(request, 'edit_profile.html', args)




@login_required()
def recipientView(request ):
    # context= {}
    # form = RequesterForm(request.POST)
    # context['form'] = form

    args = {'user': request.user}

    if request.method == "POST":

        context = {}
        form = RecipientForm(request.POST)
        form.instance.user = request.user
        context['form'] = form
        if form.is_valid():

            form.save()
            return redirect('home')
    else:
        form = RecipientForm()
    return render(request, 'recipient.html', {'form': form}, )



class RequesterUpdate(UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = "edit_requester.html"
    success_url = 'profile'

    def getobject(self, *args, **kwargs):
        user_ = self.request.user
        return get_object_or_404(User, user=user_)
