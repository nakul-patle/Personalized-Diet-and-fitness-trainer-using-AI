from django.shortcuts import render,get_object_or_404,redirect
from .implementation import execute_pushup, execute_bicep,executePoseEstimation
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact,Bookapp

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coach(request):
    return render(request, 'coach.html')

def service(request):
    if 'pushup' in request.GET:
        execute_pushup()
    if 'bicep' in request.GET:
        execute_bicep()
    if 'posedetect' in request.GET:
        executePoseEstimation()
        
        
    # if request.method == 'POST':
    #     print("hello")
    #     execute()
        
    return render(request, 'service.html')

def bookapp(request):
    if request.method =='POST':
        
        fname=request.POST['fname']
        lname=request.POST['lname']
        
        ba=Bookapp(fname=fname,lname=lname)
        
        ba.save()
        messages.add_message(request, messages.SUCCESS, 'Your query has been submitted,we will get back to you soon')
      
    return render(request,'home.html')
    

def contact(request):
       
    
    if request.method =='POST':
        
        name=request.POST['name']
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
      
        
        
       
        
            
        
        contact=Contact(name=name,email=email,subject=subject,message=message)
        
        contact.save()
      
    
       
        
        messages.add_message(request, messages.SUCCESS, 'Your query has been submitted,we will get back to you soon')
        
        
        return redirect('contact-us')
    
    
        
    return render(request,'contact.html')


def success_story(request):
    return render(request, 'success_story.html')


def blog(request):
    return render(request, 'blog.html')



    
    