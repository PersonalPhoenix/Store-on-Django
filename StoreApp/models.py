from django.db import models
from django.utils import timezone


class ProductCard(models.Model):
    '''models products cards'''

    class StatusProductCard(models.TextChoices):
        '''status product card: published / draft'''

        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
     # status product card: published / draft
    status = models.CharField(max_length = 2,
                              choices = StatusProductCard.choices,
                              default = StatusProductCard.DRAFT)
    
    # body product card
    title = models.CharField(max_length = 50)
    sub_description = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    characteristics = models.JSONField()
    image = models.ImageField(upload_to = 'products/% Y/% m/% d/', 
                              height_field = 300, 
                              width_field = 300,
                              unique = True,
                              null = False)
    
    # for url adres
    slug = models.SlugField(max_length = 50, unique_for_date = 'publish')

    def __str__(self) -> str:
        return self.title, self.sub_description, self.description

    class BrandsProductCard(models.Model):
        '''brands each products cards'''

        pass

    class TagsProductCard():
        '''tags each products cards'''

        pass

    # for ordering in class Meta
    publish = models.DateTimeField(default = timezone.now)

    class Meta:
        '''sort and index products cards'''

        ordering = ['-publish']
        indexes = [models.Index(fields = [ '-publish'])]