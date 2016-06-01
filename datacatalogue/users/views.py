from django.http import HttpResponse
from django.shortcuts import render

from .models import LDAP
from .models import Contact
from .models import Tenant

# Create your views here.


def post_create(request):
	
	return HttpResponse("<h1>Create</h1>")


def post_detail(request):
	context = {
		"title": "Detail"
	}
	return render(request, "index.html", context)
	# return HttpResponse("<h1>Detail</h1>")


def post_list(request):
	queryset = LDAP.objects.all()
	queryset = Contact.objects.all()
	queryset = Tenant.objects.all()
	context = {
		"object_ldap": queryset,
		"object_contact": queryset,
		"object_tenant": queryset,
		"title": "List"
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User List"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}
	return render(request, "index.html", context)
	# return HttpResponse("<h1>List</h1>")


def post_update(request):
	
	return HttpResponse("<h1>Update</h1>")


def post_delete(request):
	
	return HttpResponse("<h1>Delete</h1>")
