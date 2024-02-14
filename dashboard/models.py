from django.db import models

CATEGORY = (
    ('papelaria','papelaria'),
    ('eletronico','eletronico'),
    ('comida','comida'),
    
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices = CATEGORY , null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.name} - {self.quantity}'
