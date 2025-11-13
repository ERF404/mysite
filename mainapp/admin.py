from django.contrib import admin
from mainapp.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ['subject', 'message']

admin.site.register(Contact, ContactAdmin)
