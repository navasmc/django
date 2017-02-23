from django.conf.urls import url

from . import views
app_name = 'user'
urlpatterns = [
     # ex: /login/
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
   
]