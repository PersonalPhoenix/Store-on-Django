from django.contrib import admin
from .models import ProductCard


admin.site.register(ProductCard)

@admin.register
class ProductCardAdmin(admin.ModelAdmin):

    #отображаемые поля 
    list_display = ['title', 'sub-descriprion', 'description',
                    'price', 'characteristics', 'slug', 
                    'image', 'publish', 'status',]
    
    #фильтр постов
    list_filter = ['status', 'created', 'publish']
    
    #поле поиска
    search_fields = ['title', 'body']

    #автозаполнение slug при создании поста
    prepopulated_fields = {'slug': ('title')}

    #навигация по датам
    date_hierarchy =  'publish'

    #фильтр постов по умолчанию
    ordering = ['status', 'publish']