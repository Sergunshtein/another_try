from django.contrib import admin
from .models import Contacts # file models is in the same dir 


class ContactAdmin (admin.ModelAdmin):
    list_display=('id','name','listing','email','contact_date')  #whats displayd in contact table in admin
    list_display_links = ('id','name')
    search_fields = ('name',"email", 'listing')
    list_per_page = 25

admin.site.register (Contacts,ContactAdmin)
                      # model|  classname