from django.contrib import admin
from .models import Drawing, Category


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
