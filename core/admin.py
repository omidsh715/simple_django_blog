from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'pre_context', 'published', 'create_date']


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['email','tel','telegram']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title','status']