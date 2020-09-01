#from urllib3 import request
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView

from .forms import RequesterForm, RecipientForm, RegistrationForm, RegisterUpdateForm, UpdatePasswordForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, FormView
from .models import Recipient, Requester, User

from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import views as auth_views, authenticate, login


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required()
def dashboardView(request):
    return render(request, 'dashboard.html')


def logoutview(request):
    return render(request, 'registration/logged_out.html')

class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


# def registerView(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#
#             return redirect('login_url')
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'registration/register.html', {'form': form})


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

class ViewProfile(generic.DetailView):
    model = User
    template_name = 'profile.html'


def edit_profile(request):
    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile', pk=request.user.pk)

    else:
        form = RegisterUpdateForm(instance=request.user)
        args= {'form': form}
        return render(request, 'edit_profile.html', args)

@login_required()
def edit_password(request):
    if request.method == 'POST':
        form= UpdatePasswordForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile', pk=request.user.pk)
    else:
        form=UpdatePasswordForm()
        args={'form': form}
        return render(request, 'password.html', args)

# def dictcreate(request):
#     context_dict = {
#         'user': request.self.user.name,
#         'business': 'staffing advantage llc',
#         'email': request.self.email,
#         'company address1': request.self.user.address_line1,
#         'address2': request.self.user.address_line2,
#         'city': request.self.user.city,
#         'state': request.self.user.state_or_territory,
#         'zipcode': request.self.user.zipcode,
#     }
#     return context_dict
#  def render_to_pdf(template_src, context_dict={}, request):
#     template = get_template('COIDoc.html')
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='applicaiton/pdf')
#     return None
#
#
# class ViewPDF(View):
#
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('accounts/COIDoc.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')






@login_required()
def recipientView(request):

    # def render_to_pdf(, context_dict={}, request):
    #     template = get_template('COIDoc.html')
    #     html = template.render(context_dict)
    #     result = BytesIO()
    #     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    #     if not pdf.err:
    #         return HttpResponse(result.getvalue(), content_type='application/pdf')
    #     return None

    #args = {'user': request.user}

    if request.method == "POST":

        context = {}
        newdict= {   }
        form = RecipientForm(request.POST)
        form.instance.user = request.user
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipientForm()
    return render(request, 'recipient.html', {'form': form}, )


def RequesterUpdate(request):
    model = User
    form_class = RegisterUpdateForm()
    template_name = "edit_requester.html"
    success_url = 'profile'

   # def getobject(self, *args, **kwargs):
   #      user_ = self.request.user
   #      return get_object_or_404(User, user=user_)






def loginview(request):
    if request.method == "POST":

        context = {}
        form = AuthenticationForm(None, request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            ...

        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form}, )








# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             form=
#             return render(request, 'logged_in.html')
#         else:
#             return render(request, 'login.html',
#                 {'message': 'Bad username or password'}
#             )
#     else:
#         return render(request, 'login.html')
