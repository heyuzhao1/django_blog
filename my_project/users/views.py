from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from . import forms
from . import models

# Create your views here.
def register_view(request):
    if request.method =="POST":
        form = forms.CreateUser(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
              
    else:
        form =  forms.CreateUser()
    return render(request,"users/register.html",{"form":form})

def login_view(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if 'next' in request.POST:
                #request.POST 是一个包含所有通过 POST 方法发送到服务器的数据的字典
                return redirect(request.POST.get('next'))
            #如果url中含有post字段则重定位到next指定的链接
            else:
                return redirect('posts:list')
    else:
        form = AuthenticationForm()
    return render(request,"users/login.html",{"form":form})

def logout_view(request): 
    if request.method=="POST":
        logout(request)
        return redirect('posts:list')

def profile_view(request):
    
    #load entire information from models/database
    user_profile = get_object_or_404(models.UserProfile,user=request.user)
   
    if request.method =="POST":
        # print("POST request received")
        #Then create  table through the forms function
        form= forms.UserProfileForm(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            # print("Form is valid")
            form.save()
            return redirect('posts:list')# 保存成功后重定向到个人信息页面
        else:
             print("Form is invalid", form.errors)
    else:
        form  = forms.UserProfileForm(instance=user_profile)
    return render(request,"users/profilePage.html",{"form":form})

