from django.contrib import admin

# Register your models here.
from .models import product,category


class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)



class productadmin (admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']

    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['stock', 'price', 'available']
admin.site.register(product,productadmin)