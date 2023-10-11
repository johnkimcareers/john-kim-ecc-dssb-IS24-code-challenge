from django.db import models

class Product(models.Model):
    productId = models.TextField()
    productName = models.CharField(max_length=100)
    productOwnerName = models.CharField(max_length=50)
    developers = models.JSONField()
    scrumMasterName = models.CharField(max_length=50)
    startDate = models.DateField()
    methodology = models.TextField()
    location = models.TextField()
