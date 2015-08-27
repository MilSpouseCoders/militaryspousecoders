from django.conf.urls import url
 
from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^register$', views.register, name='register'),
 url(r'^signup$', views.signup_form, name='signup'),
 url(r'^login$', views.login_form, name='login'),
 url(r'^login_user$',views.login_user, name='login_user'),
 url(r'^logout$', views.logout_view, name='logout_view')
]
