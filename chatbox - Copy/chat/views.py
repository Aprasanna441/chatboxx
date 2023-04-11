from django.shortcuts import render
from .models import Chat,Group


from django.shortcuts import render

#Create your views here.
from ast import Not
from asyncio.windows_events import NULL
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

from django.contrib.auth.decorators import login_required

import datetime
from django.contrib.auth.models import User

from django.contrib.auth import authenticate , login as loginUser , logout
from django.views.generic import TemplateView

#Create your views here.

@login_required(login_url='login')
def welcome(request):
    return render(request,'Templates/welcomepage.html')




def login(request):
        user=request.user
        
    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return render(request,"Templates/welcomepage.html")
                

                
        
        
    
   
        return render(request,"Templates/loginsignup.html",{'formauth':AuthenticationForm,'formsignup':UserCreationForm})

def signup(request):
    form=UserCreationForm(request.POST)
    
    if form.is_valid():
        user=form.save()

        if user is not None:
            loginUser(request , user)
            return render(request,"Templates/welcomepage.html")
            
            
    return render(request,"Templates/loginsignup.html",{'formsignup':UserCreationForm,'formauth':AuthenticationForm})






def signout(req):
    logout(req)
    return redirect('signup')

@login_required(login_url='login')
def index(request,group_name):
    
    group=Group.objects.filter(name= group_name).first()
    chats=[]
    
    if group:
        chats=Chat.objects.filter(group=group)
    else:
        
        group=Group(name =group_name)
        group.save()
        
        
    return render(request,'Templates/index.html',{'chats':chats,'group':group})


class GroupChatView(TemplateView):
    template_name="Templates/index.html"
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        te=self.kwargs['groupname']
        
        
                
        # idd=Group.objects.get(name=te).getid()
        group=Group.objects.filter(name= te).first()
        chats= Chat.objects.filter(group=group)
        context['groupname']=self.kwargs['groupname']
        context['chats']=chats
        
       
        return context
        



        
        

class IndividualChatView(TemplateView):
    template_name="Templates/individualchat.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users']=User.objects.filter(is_online=True)
        return context
        
        
    
        
        
        
        
    