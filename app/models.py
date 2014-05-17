from django.db import models

# Create your models here.

class Sheet(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=250)
    deleted = models.BooleanField(default=False)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)
    parent = models.IntegerField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    opens = models.TimeField()
    closes = models.TimeField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    date = models.DateTimeField()
    price = models.IntegerField()
    shop = models.ForeignKey(Shop)
    deleted = models.BooleanField(default=False)
    weight = models.IntegerField()
    count = models.IntegerField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Set(models.Model):
    item = models.ForeignKey(Item)
    date = models.DateTimeField()
    sheet = models.ForeignKey(Sheet)
    purshased = models.BooleanField(default=False)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.id


