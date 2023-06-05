from django.shortcuts import render
from taggit.models import Tag

from .models import ProductCard

class ViewProductCard:

    queryset = ProductCard.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'templates/StoreApp/product_card_in_home_page.html'