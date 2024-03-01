from django.contrib import admin
from global_page.models import PageGlobalVeraibles,PageTextVeraibles
from .models import Category, Comments, FruitCarts
# Register your models here.


@admin.register(PageGlobalVeraibles)
class PageGlobalVeraiblesAdmin(admin.ModelAdmin):
    list_display = ('id','image') 
    list_editable = ('image',)
    
@admin.register(PageTextVeraibles)
class PageTextVeraiblesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_editable = ('title',)
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')
    list_display_links = ('category_name',)
    list_filter = ('id', )
    
    
@admin.register(FruitCarts)
class FruitCartsAdmin(admin.ModelAdmin):
    list_display = ('id','fruit_name', 'category')
    list_display_links = ('fruit_name',)
    
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name')
    list_display_links = ('user_name',)
    
    
admin.site.site_header = 'Online Fruits shop Admin Page'