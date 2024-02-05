from django.contrib import admin
from home.models import Contact
from blog.models import Post, BlogComment

# Register your models here.
admin.site.register(Contact)
admin.site.register((Post,BlogComment))
