from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "egfdatabase"
urlpatterns = [
    path('egf', views.index, name='egf'),
    path('home', views.base, name='home'),
    path('index', LoginView.as_view(template_name='egf/index.html'), name='index'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('evaluation', views.evaluation, name='evaluation'),
]