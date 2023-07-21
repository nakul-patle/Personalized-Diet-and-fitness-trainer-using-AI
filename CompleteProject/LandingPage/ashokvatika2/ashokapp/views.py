from datetime import date
from django import views
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.tokens import default_token_generator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from .form import SignupForm
from django.utils.encoding import force_bytes
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *
from .models import User
from .models import Category
import razorpay

 # Create your views here
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_protect

# from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator


def Food(request):
    if(request.method == "POST"):
        dname=request.POST.get('dname')
        dlname=request.POST.get('dlname')
        demail=request.POST.get('demail')
        dphone=request.POST.get('dphone')
        daddress=request.POST.get('daddress')
        dAadhaar=request.FILES['Aadhaar']
        dplant=request.POST.get('plant')
        dcountplants=request.POST.get('countplants')
        dplantsimage=request.FILES['plantsimage']
        print(dname,dlname,demail,dphone,daddress, dAadhaar,dplant,dcountplants,dplantsimage)
        donar1=donar(name=dname,lname=dlname,email=demail,phone=dphone,address=daddress,Aadhaar=dAadhaar,plant=dplant,countplants=dcountplants,plantsimage=dplantsimage)
        donar1.save()
        print("hii")
   
      
    return render(request,'food.html')
def Fitness(request):
    if(request.method == "POST"):
        dname=request.POST.get('dname')
        dlname=request.POST.get('dlname')
        demail=request.POST.get('demail')
        dphone=request.POST.get('dphone')
        daddress=request.POST.get('daddress')
        dAadhaar=request.FILES['Aadhaar']
        dplant=request.POST.get('plant')
        dcountplants=request.POST.get('countplants')
        dplantsimage=request.FILES['plantsimage']
        print(dname,dlname,demail,dphone,daddress, dAadhaar,dplant,dcountplants,dplantsimage)
        donar1=donar(name=dname,lname=dlname,email=demail,phone=dphone,address=daddress,Aadhaar=dAadhaar,plant=dplant,countplants=dcountplants,plantsimage=dplantsimage)
        donar1.save()
        print("hii")
   
      
    return render(request,'Fitness.html')
def index(request):
   
   
    num_post = User.objects.filter().count()
    cat=Category.objects.filter().count()
    
    return render(request, 'index.html',{'count':num_post,'types':cat})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if(request.method == "POST"):
        name=request.POST.get('name')
        email=request.POST.get('semail')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request, 'contact.html')

# def services(request):
#     products=Product.get_all_products()
#     return render(request,'services.html',{'products':products})

# class plants(View):
#     def post(self,request):
#         product=request.POST.get('product')
#         remove=request.POST.get('remove')
#         cart=request.session.get('cart')
#         if cart:
#             quantity=cart.get(product)
#             if quantity:
#                 if remove:
#                     if quantity<=1:
#                         cart.pop(product)
#                     else :
#                         cart[product]=quantity-1
#                 else :
#                     cart[product]=quantity+1
               
               
#             else:
#                 cart[product]=1
#                 cart[product]=1
#         else:
#             cart={}
#             cart[product]=1
#         request.session['cart']=cart
#         print("cart", request.session['cart'])
#         return redirect('products')
    
#     def get(self,request):
#         products=None
#         cart=request.session.get('cart')
#         if not cart:
#             request.session['cart']={}
        
#         category=Category.get_all_category()
#         categoryID=request.GET.get('category')
#         if( categoryID):
#             products=Product.get_all_products_by_categoryid(categoryID)
#         else :
#             products=Product.get_all_products()
#         paginator = Paginator(products,30)
#         page_number=request.GET.get('page')
#         page_obj=paginator.get_page(page_number)
#         nums="a"*page_obj.paginator.num_pages
#         data={}
#         data['products']=products
#         data['category']=category
#         data['page_obj']=page_obj
#         data['nums']=nums
#         return render(request,'plants.html',data)



   

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            email=form.cleaned_data.get('email')
            user.save()
            # '127.0.0.1:8000'                                           #get_current_site(request)
            current_site = get_current_site(request)
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,  # '127.0.0.1:8000' , current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),


                'token': account_activation_token.make_token(user),
            })
            subject = 'Activate Your  Account'
            user.email_user(subject, message)
        
            emailsend=EmailMessage(subject,message,from_email=settings.EMAIL_HOST_USER,to=[email])
            emailsend.send()
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect('account_activation_sent')
        
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def LoginUser(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['customer_id']=User.id
            request.session['username']=user.get_username()
            messages.add_message(request, messages.SUCCESS,
                                 "Successfully Login.")
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.add_message(request, messages.ERROR,
                                 "You don't have an account.")
            return render(request, 'login.html')
    return render(request, 'login.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

def LogoutUser(request):
    request.session.clear()
    logout(request)
    return redirect('home')


# class cart(View):
#     def get(self,request):
#         ids=(request.session.get('cart'))
#         products=Product.get_product_id(list(ids))
#         # print(ids)

       
#         return render(request,'cart.html',{'cart':products})
   


# def Checkout(request):
#     address=request.POST.get('address')
#     phone=request.POST.get('phone')
#     customer=request.session.get('customer_id')
#     cart=request.session.get('cart')
#     ids=(request.session.get('cart'))
#     products=Product.get_product_id(list(ids))
    
#     amount1=int(request.POST.get('price'))
#     amount=amount1*100
#     print(amount)

#     client = razorpay.Client(auth=("rzp_test_clZsiMXMKNtjFn", "06is0laXVE7fwlmJH4clRb10"))      
#     data={
#        'amount':amount1*100,
#        "currency":"INR",
#        "receipt":"feelfreeto code",
#        }
  
   
#     payment=client.order.create(data=data)
   
#     for i in products:
#         print("checkout",cart.get(str(i.id)))
#         order=Order(
#                     products=i,
#                     image=i.image,
#                     name=i.name,
#                     payment_id=payment['id'],
#                     customer=customer,
#                     quantity=cart.get(str(i.id)),
#                     price=i.price,
#                     Address=address,
#                     phone=phone
#                     )
#         order.save()
#     return render(request,'payment.html',{'cart':products,'payment':payment})
       
            
 

      
# class order_customer(View):
#     def get(self,request):
#         customer=request.session.get('customer')
#         orders=Order.get_orders_by_customer(customer)
#         return render(request,'order.html',{'orders':orders})

# def payment(request):      
       
#     return render(request,'payment.html')
       