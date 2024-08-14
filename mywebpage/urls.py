from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('test/', views.testPage, name='test-page'),
    path('color/', views.cardclrPage, name='cardcolor'),
    path('loop/', views.testloopPage, name='teloop'),
    path('from/', views.from_testPage, name='from_ts')
]
