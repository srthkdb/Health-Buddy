from .models import Type
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "users/base_home.html"

class Calc(TemplateView):
    template_name = "users/health_calc.html"

class Contact(TemplateView):
    template_name = "users/contact_us.html"

class Profile(TemplateView):
    template_name = "users/Profile.html"

class UserFormView(View):
    #Credits: code structure for this class is adapted from newboston django video tutorials.
    form_class = UserForm
    template_name = 'users/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user_type = form.cleaned_data['user_type']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            if password1!=password2:
                return render(request, self.template_name, {'form': form})
                
            #create user
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            #create type
            types = Type(
                user = user,
                types = user_type,
            )
            types.save()
            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password2)
              
            if user is not None:
                #django gives admin power to suspend users. This option checks if the user is not suspended.
                if user.is_active:
                    login(request, user)
                    if type == 'phr':
                        return render(request, 'users/phr_register.html', {'form': form, 'user': user})
                    if type == 'rec':
                        return render(request, 'users/rec_register.html', {'form': form, 'user': user})
                    if type == 'doc':
                        return render(request, 'users/doc_register.html', {'form': form, 'user': user})
                    if type == 'pat':
                        return render(request, 'users/pat_register.html', {'form': form, 'user': user})
        return render(request, self.template_name, {'form': form})

