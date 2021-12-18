from django.db import models

# Create your models here.
class profile(models.Model):
    first_name = models.CharField(max_length=100,null=False, help_text="please enter your own name")
    last_name = models.CharField(max_length=100,null=False, help_text="please enter your father's name")
    
    def __str__(self):
        return f"{self.last_name.upper()} {self.first_name}"
