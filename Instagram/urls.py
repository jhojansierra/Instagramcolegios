from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html' ,redirect_authenticated_user=True),name= 'login'),
    url(r'^Logout/$', auth_views.LogoutView.as_view(),name='Logout'),
    url(r'^electro/$', views.electro, name = 'electro'),
    url(r'^avicii/$', views.avicii, name = 'avicii'),





]
