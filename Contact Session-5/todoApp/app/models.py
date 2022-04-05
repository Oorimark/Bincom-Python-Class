from email.policy import default
from django.db import models

# Create your models here.

class Todolist(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name;
    
class list(models.Model):
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    lists = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
     
    def __str__(self) -> str:
        return self.lists
    
 
        
