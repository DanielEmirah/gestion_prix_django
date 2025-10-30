from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # Nom du produit (texte court)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix d'achat
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix de vente
    margin = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Marge calculée
    updated_at = models.DateTimeField(auto_now=True)  # Date de dernière modification automatique

    # Méthode spéciale pour afficher le nom du produit dans l’admin Django
    def __str__(self):
        return self.name

    # Méthode pour calculer la marge automatiquement
    def save(self, *args, **kwargs):
        # Calcule la marge avant de sauvegarder le produit
        self.margin = self.selling_price - self.purchase_price
        super().save(*args, **kwargs)  # Appel de la méthode save() originale
