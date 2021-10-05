from django.contrib import admin
from django.urls import path
from home.views import *


admin.site.site_header = "Raj Tours Admin"
admin.site.site_title = "Raj Tours Admin Portal"
admin.site.index_title = "Welcome to Raj Tours"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name='home'),
    path("about/",about,name='about'),
    path("services/",services,name='services'),
    path("contact/",contactUs,name='contact'),
    path("login/",loginUser,name="login"),
    path("logout/",logoutUser,name="logout" ),
]



