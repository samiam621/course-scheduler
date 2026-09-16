from django.db import models

# Create your models here.

class Course(models.Model):
    subject = models.CharField(max_length=5)
    course_number= models.CharField(max_length=5)
    title=models.CharField(max_length=200)
    credits=models.IntegerField()

    def __str__(self):
        return(f"{self.subject}{self.course_number}: {self.title}   {self.credits}")