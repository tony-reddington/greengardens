from django.contrib import admin
from .models import BlogPost

# Field to display on the admin panel
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publish_date',
    )

admin.site.register(BlogPost, BlogPostAdmin)
