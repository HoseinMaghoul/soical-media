from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import UserRegisterForm, UserLoginForm, ProfileImageForm 
from .models import Profile, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'


    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'] , password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you are login successfuly', 'info')
                return redirect('core:home')
        



class UserRegister(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            Profile.objects.create(user=user)
            messages.success(request, 'registreion is successfuly', 'info')
            return redirect('core:home')
        return render(request, self.template_name, {'form':form})



class UserLogout(LoginRequiredMixin, View):
    
    def get(self, request):
        logout(request)
        messages.success(request, 'ypu logout successfuly', 'info')



class UserDashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    form_class = ProfileImageForm

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, self.template_name, {'user':user, 'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'upload successfuly', 'info')
            return redirect('accounts:dashboard', request.user.username)
