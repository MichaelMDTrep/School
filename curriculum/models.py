from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class CourseCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Course Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Course(models.Model):

     title= models.CharField(max_length=350)
     content= models.TextField(max_length=10000)
     category = models.ForeignKey("CourseCategory", on_delete=models.SET_NULL, null=True)

     def __str__(self):
        return self.title


class CourseCompleted(models.Model):

     user = models.ForeignKey(User, on_delete=models.CASCADE) 
     date = models.DateField(default=date.today)
     course = models.ForeignKey("Course", on_delete=models.CASCADE)

     def __str__(self):
        return f'{self.user} completed {self.course} on {self.date}'


class CourseLink(models.Model):
      
      name = models.CharField(max_length=350)
      course = models.ForeignKey("Course", on_delete=models.CASCADE)
      link = models.URLField(max_length=350)

      def __str__(self):
        return self.name