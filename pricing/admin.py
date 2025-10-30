from django.contrib import admin
from .models import Product

# Enregistrement du modèle dans l’interface admin
admin.site.register(Product)