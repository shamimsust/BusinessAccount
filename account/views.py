from django.shortcuts import render, redirect
from django.contrib import auth, messages



# Create your views here.
def index(request):
    return render(request,"index.html")
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            return redirect('home')
 
        else:
            messages.error(request, 'Error wrong username/password')
            redirect('login')
 
    return render(request, 'login.html')
    
    
def logoutuser(request):
    auth.logout(request)
    return redirect('home')