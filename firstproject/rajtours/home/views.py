from home.models import Contact
from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
# @login_required()
def index(request):
    if request.user.is_authenticated:
        templates = 'index.html'
        return render(request,templates)
    else:
        return redirect('/login')
# @login_required()
# def index(request):
#     templates = 'index.html'
#     return render(request,templates)
    # return HttpResponse("this is home page")

# @login_required()
def about(request):
    templates = 'about.html'
    return render(request,templates)
    # return HttpResponse("this is about page")

# @login_required()
def services(request):
    templates = 'services.html'
    return render(request,templates)
    # return HttpResponse("this is services page")  

# @login_required()
def contactUs(request):
    templates = "contact.html"
    if request.method == "POST":
        print("------------------------------",request.POST)
        print("firstname",request.POST["firstname"])
        print("lastname",request.POST["lastname"])
        print("email",request.POST["email" ])
        print("phone",request.POST["phone"])
        print("city",request.POST["city"])
        print("state",request.POST["state"])
        print("zip",request.POST["zip"])
 
        obj,created=Contact.objects.get_or_create(firstname= request.POST['firstname'],lastname= request.POST['lastname'],email= request.POST['email'],phone= request.POST['phone'],city= request.POST['city'],state= request.POST['state'],zip= request.POST['zip'])
        print('obj and created',obj,created)

        if created:
            messages.success(request, 'New entry created')
        else:
            messages.info(request, 'Entry already exist')

    templates = "contact.html"    
    return render(request,templates)
    # return HttpResponse("this is services page")
# @login_required()   
def loginUser(request):
    templates = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
           messages.warning(request, 'Username/Password does not exist') 
    templates = 'login.html'
    return render(request,templates)
# @login_required()
def logoutUser(request):
    templates = 'login.html'
    logout(request)
    return render(request,templates)        







