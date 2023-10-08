from django.db import models
from django.shortcuts import reverse
from Admin.models import books

# Create your models here.

class students(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,unique=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)


    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f'/media/{self.image}'
    
    def get_show_url(self):
        return reverse('student.detail',arge=[self.id])
    
    def get_delete_url(self):
        return reverse('student.delete',args=[self.id])
    
    def get_edit_url(self):
        return reverse('student.edit',args=[self.id])
    

