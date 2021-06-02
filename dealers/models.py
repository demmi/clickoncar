from django.db import models
from catalog import models as catalog


class Dealer(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    url = models.URLField()
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=False)
    coordinates = models.CharField(max_length=50, blank=False)
    brand = models.ForeignKey(catalog.Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
