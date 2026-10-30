from myapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('api/hello/', views.api_hello, name='api_hello'),
    path('about/', views.about, name='about'),
]