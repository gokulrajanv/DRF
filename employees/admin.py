from django.contrib import admin
from .models import Department, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'designation', 'salary', 'joining_date', 'is_active', 'department', 'manager')
    list_filter = ('department', 'manager')
    search_fields = ('full_name', 'email')
    list_editable= ('is_active','salary')

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)
                    
# Register your models here.

# admin.site.register(Employee, EmployeeAdmin) here the EmployeeAdmin is used to customize the admin interface for the Employee model.