from django.contrib import admin
from blog.models import Post 
# Register your models here.
@admin.register(Post)
class postadmin(admin.ModelAdmin):
    list_display = ['id','author','title','text','created_date','published_date']
