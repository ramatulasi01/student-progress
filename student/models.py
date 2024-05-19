from django.db import models

class Studentprogress(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    marks=models.CharField(max_length=100,blank=True)
    result=models.CharField(max_length=6)
    grade=models.CharField(max_length=5)
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.name
    