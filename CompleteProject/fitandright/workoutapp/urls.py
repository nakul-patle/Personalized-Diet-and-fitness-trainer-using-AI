from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home-page"),
    path('about/', views.about, name="about"),
    path('coach/', views.coach, name="coach"),
    path('service/',views.service, name="service"),
    path('contact/',views.contact,name="contact-us" ),
    path('bookapp/',views.bookapp, name="book-app"),
    path('blog/', views.blog, name="blog"),
    path('success_story/', views.success_story, name="success_stories"),
    
]