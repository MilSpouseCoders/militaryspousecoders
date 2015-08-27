from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('members:login'))
 	return render(request, 'members/index.html', {})

def signup_form(request):
	return render(request, 'members/signup.html', {})

def login_form(request):
	return render(request, 'members/login.html', {})

def register(request):
	print request.POST
	user = User.objects.create_user(username = request.POST['user_name'], email = request.POST['email'], password = request.POST['password'])
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.save()
	user = authenticate(username = request.POST['user_name'], password = request.POST['password'])
	login(request, user)
	return HttpResponseRedirect(reverse('members:index'))

def login_user(request):
	user = authenticate(username = request.POST['user_name'],password = request.POST['password'])
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('members:index'))
		return HttpResponseRedirect(reverse('members: login'))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('members:login'))

