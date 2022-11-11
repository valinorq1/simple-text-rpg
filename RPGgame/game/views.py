from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render
from django.views import View
from loguru import logger
from users.models import CustomUser

from .forms.forms import LoginForm, UserRegisterForm


class LoginView(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

        return render(request, self.template_name, {'form': form})
    
    
class RegisterView(View):
    form_class = UserRegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('registered successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

        return render(request, self.template_name, {'form': form})
    
