from django.contrib import admin
from blog.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_view','author', 'status', 'created_date', 'published_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)