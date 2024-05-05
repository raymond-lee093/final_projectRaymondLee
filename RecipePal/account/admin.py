from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account


# Due to creating new user model, must tell admin site how to use it
class AccountAdmin(UserAdmin):
	# Display these fields in admin site
	list_display = ('username','email','date_joined', 'last_login', 'is_admin','is_staff')
	# Fields that are allowed to be searched in admin site
	search_fields = ('email','username',)
	# Fields that cannot be changed in admin site
	readonly_fields = ('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


# Register new admin with Account model
admin.site.register(Account, AccountAdmin)