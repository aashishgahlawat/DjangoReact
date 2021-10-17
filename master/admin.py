from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MasterCountry, MasterState, MasterCity, MasterBusiness, MasterCustomer
from import_export.admin import ImportExportModelAdmin

# admin.site.register(User)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'is_active']


class MasterCountryAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'code', 'dial_code']
    ordering = ['-name']


admin.site.register(MasterCountry, MasterCountryAdmin)


@admin.register(MasterState)
class MasterStateAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ['country_name', 'name', 'code', 'tin']

    @staticmethod
    def country_name(self):
        return self.country.name

    country_name.admin_order_field = 'name'
    country_name.short_description = "Country Name"


@admin.register(MasterCity)
class MasterCityAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'pincode']
    list_display = ['name', 'pincode']


@admin.register(MasterCustomer)
class MasterCustomerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'email']
    list_display = ['name', 'phone', 'email']


@admin.register(MasterBusiness)
class MasterBusinessAdmin(admin.ModelAdmin):
    search_fields = ['display_name', 'phone', 'email']
    list_display = ['display_name', 'phone', 'email']








