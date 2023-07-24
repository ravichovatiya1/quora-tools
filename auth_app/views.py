from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from django.contrib import auth
from auth_app import models, forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView, FormView


# Create your views here.

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'auth_app/signup.html'
    success_url = reverse_lazy('auth_app:sign_in')

    def form_valid(self, form):
        # Hash the password before saving the user instance
        form.instance.password = make_password(form.cleaned_data['password'])
        messages.success(self.request, f'Registration Successful !' )
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('quora_app:index'))
        else:
            return super().get(request, *args, **kwargs)


class SignInView(FormView):
    form_class = forms.SigninForm
    template_name = 'auth_app/signin.html'
    success_url = reverse_lazy('index:index') 

    def form_valid(self, form):
        user_cred = models.User.objects.filter(email=form.data['email'].lower())
        if not user_cred:
            messages.error(self.request, 'Invalid credentials. Please try again.')
            return self.form_invalid(form)

        user = auth.authenticate(
            username=user_cred.first().username,
            password=form.data['password']
        )
        if user is not None:
            auth.login(self.request, user)
            messages.success(self.request, 'Login Sucessful.')
            next_url = self.request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid credentials. Please try again.')
            return self.form_invalid(form)
        
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('index:index'))
        else:
            return super().get(request, *args, **kwargs)
        
class LogOutView(LogoutView):
    next_page = reverse_lazy('auth_app:sign_in')
            
        
