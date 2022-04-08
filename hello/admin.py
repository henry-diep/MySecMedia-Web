from django.contrib import admin
from .models import NewsItem, Author, Feedmodel
# Register your models here.
admin.site.site_header = 'My Security Media DJANGO Admin'

admin.site.register(NewsItem)
admin.site.register(Feedmodel)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
