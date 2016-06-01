from django.contrib import admin

# Register your models here.

from .models import LDAP
from .models import Contact
from .models import Tenant


class LDAPModelAdmin(admin.ModelAdmin):
	list_display = ["dc", "uid", "o"]
	list_display_links = ["uid"]
	list_editable = ["dc"]
	list_filter = ["uid", "o"]

	search_fields = ["o", "street"]

	class Meta:
		model = LDAP


class ContactModelAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name"]
	list_display_links = ["last_name"]
	list_editable = ["first_name"]
	list_filter = ["first_name", "last_name"]

	search_fields = ["first_name", "phone_number"]
	
	class Meta:
		model = Contact


class TenantModelAdmin(admin.ModelAdmin):
	list_display = ["role", "url"]
	list_display_links = ["url"]
	list_editable = ["role"]
	list_filter = ["role", "url"]

	search_fields = ["role", "url"]
	
	class Meta:
		model = Tenant
			
		
admin.site.register(LDAP, LDAPModelAdmin)
admin.site.register(Contact, ContactModelAdmin)
admin.site.register(Tenant, TenantModelAdmin)

