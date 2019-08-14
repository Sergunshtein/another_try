from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published',"price", "list_date","realtor")
    list_filter = ["realtor"]
    list_editable = ["is_published",'price']
    search_fields = ['title','description']
    

admin.site.register (Listing,ListingAdmin)