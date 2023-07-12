from django.contrib import admin
from . models import AddContact

# Register your models here.
@admin.register(AddContact)
class AddContAdmin(admin.ModelAdmin):
    list_display=['id','name','phone1','phone2','email','picture','address','business_key','textfield']