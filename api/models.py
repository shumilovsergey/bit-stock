from django.db import models
from django.utils import timezone

class TelegramUsers(models.Model):
    session_id = models.CharField(max_length=56, unique=True)
    tg_id = models.CharField(max_length=56, default="no-auth")
    name = models.CharField(max_length=56, default="no-auth")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tg_id
    class Meta:
        ordering = ['-created']

class Orgs(models.Model):
    boss_tg = models.CharField(max_length=56, default="no-auth")
    name = models.CharField(max_length=56, default="no-name")
    created = models.DateTimeField(default=timezone.now)
    workers = models.ManyToManyField(TelegramUsers)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']

class Categories(models.Model):
    name = models.CharField(max_length=56, default="no-name")
    org = models.ForeignKey(Orgs, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']

class Products(models.Model):
    name = models.CharField(max_length=56, default="no-name")
    org = models.ForeignKey(Orgs, on_delete=models.CASCADE)
    description = models.TextField(default=None)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']
        
# PRODUCTS
# CATEGORY
# name
# description
# count

# CATEGORIES
# name

# DEALS
# type
# TELEGRAM_USER
# PRODUCT
# date
# price

