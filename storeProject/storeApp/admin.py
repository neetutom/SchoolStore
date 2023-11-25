from django.contrib import admin
from .models import Department, Course, Order

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['dept_name', 'slug']
    prepopulated_fields = {'slug':['dept_name']}
admin.site.register(Department, DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'department']
admin.site.register(Course, CourseAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'department', 'course']
admin.site.register(Order, OrderAdmin)