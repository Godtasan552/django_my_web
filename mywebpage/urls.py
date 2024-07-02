from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexPage),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
]
