from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RequesterForm, RecipientForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipient, Requesters
from django.contrib.auth.models import User


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
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


def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)




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

# class RequesterUpdate(UpdateView):
#     model = Requesters
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     form = RecipientForm(request.POST)
#     form.instance.user = request.user
#     def get_object(self):
#         return get_object_or_404(Requesters, pk=self.request.user.id)
