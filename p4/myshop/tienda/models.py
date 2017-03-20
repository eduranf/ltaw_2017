import datetime
from django.db import models
from django.utils import timezone
#En upload_to deberia poner una carpeta para cada tipo de producto(bici,CD y libro), o una generica de productos...
# Create your models here.
class Bike(models.Model):
    brand = models.CharField(blank=False,max_length=20) #No seran necesarios mas de 20 caracteres para especificar el nombre de una MIDDLEWARE_CLASSES
    model = models.CharField(blank=False,max_length=30)
    color = models.CharField(blank=False,max_length=30)
    units = models.IntegerField(blank=False)
    price_euros= models.DecimalField(blank=False,max_digits=6,decimal_places=2)#"max_digits" indica el numero total de digitos, "decimal_places", la precision decimal
    video = models.FileField(blank=False,upload_to='products',max_length=100)
    image = models.ImageField(blank=False,upload_to='products',max_length=100)
    pub_date = models.DateTimeField('date publised') #Este campo va a especificar la fecha en la que se subio el producto a la tienda
    #rate (quizas en el futuro)
    def __unicode__(self):
        return self.brand + "_" + self.model

class Book(models.Model):
    title = models.CharField(blank=False,max_length=50)
    author = models.CharField(blank=False,max_length=50,)
    topic = models.CharField(blank=False,max_length=50)
    units = models.IntegerField(blank=False)
    price_euros = models.DecimalField(blank=False,max_digits=6,decimal_places=2)
    image = models.ImageField(blank=False,upload_to='products',max_length=100,)
    pub_date = models.DateTimeField('date publised') #Este campo va a especificar la fecha en la que se subio el producto a la tienda
    def __unicode__(self):
        return self.author + "_" + self.title

class CD(models.Model):
    artist = models.CharField(blank=False, max_length=50)
    album = models.CharField(blank=False, max_length=50)
    genre = models.CharField(blank=False, max_length=50)
    cover = models.FileField(blank=False,upload_to='products',max_length=100)
    audio = models.FileField(upload_to='products',max_length=100)
    units = models.IntegerField(blank=False)
    price_euros = models.DecimalField(blank=False,max_digits=6,decimal_places=2)
    pub_date = models.DateTimeField('date publised') #Este campo va a especificar la fecha en la que se subio el producto a la tienda
    def __unicode__(self):
        return self.artist + "_" + self.album
