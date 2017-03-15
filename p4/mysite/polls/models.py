import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

# Create your models here.


#DUDAS:
    #1)Si creo una instancia de un modelo (por ejemplo, Question) y la guardo en una variable "q" en la shell de python, y luego la guardo en la base de datos,
    #se le asigna una "id". Ejemplo--> id =1.
    #2)Supongamos que ahora quiero borrar la variable "q" de la base de datos. No se restaura la id de q.
    #3)Ahora creo una nueva instancia del modelo "Question", lo guardo en una variable, lo guardo en la base de datos y se le asigna una id. En este caso,id =  2.No entiendo.

    #Crear una instancia del modelo Question.
        #// q = Question(question_text="What's new?", pub_date=timezone.now())///

    # Guardar la instancia de "Question" en la base de datos
        #q.save()

    #Eliminar una entrada en la base de datos
        #q.delete()
