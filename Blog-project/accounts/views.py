from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from blog.models import Post
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
     posts = Post.objects.all()
     return render(request, 'accounts/home.html', {'post_list': posts})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('first_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        image = request.FILES.get('image')        
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'accounts/register.html', {'error_message': error_message})
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        Profile.objects.create(user=user, phone=phone, address=address, date_of_birth=date_of_birth, image=image)
        return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # Authentication logic would go here
        try:
            profile = Profile.objects.get(phone=phone)
            user = authenticate(username=profile.user.username, password=password)
            
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Invalid credentials.'})
        except Profile.DoesNotExist:
            return render(request, 'accounts/login.html', {'error_message': 'Profile with this phone number does not exist.'})

    return render(request, 'accounts/login.html')

def logout_view(request):
    # Logout logic would go here
    logout(request)
    return redirect('home')
    # return HttpResponse("Logout successful!")

