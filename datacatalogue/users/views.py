from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import LDAPForm
from .models import LDAP
from .models import Contact
from .models import Tenant

# Create your views here.


def post_create(request):
	form = LDAPForm()
	context = {
		"form": form
	}
	return render(request, "ldap_form.html", context)


def post_detail(request, id):
	instance = get_object_or_404(LDAP, id=id)
	instant = get_object_or_404(Contact, id=id)
	inst = get_object_or_404(Tenant, id=id)
	context = {
		"title": instance.dc,
		"instance": instance,
		"title": instant.first_name,
		"instant": instant,
		"title": inst.role,
		"inst": inst
	}
	return render(request, "ldap_detail.html", context)
	# return HttpResponse("<h1>Detail</h1>")


def post_list(request):
	queryset = LDAP.objects.all(),
	queryset = Contact.objects.all(),
	queryset = Tenant.objects.all()
	context = {
		"object_ldap": queryset,
		"object_contact": queryset,
		"object_tenant": queryset,
	    "title": "List of"
	}

	return render(request, "index.html", context)
	
	# return HttpResponse("<h1>List</h1>")


def post_update(request):
	
	return HttpResponse("<h1>Update</h1>")


def post_delete(request):
	
	return HttpResponse("<h1>Delete</h1>")
