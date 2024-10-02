from django.db import models

# Create your models here.
# about model
class About (models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to = "About me")
    
    class Meta:
        verbose_name ="About me"
        verbose_name_plural="About me"
    
    def __str__(self):
        return"About me"
        
        
# service model
class project (models.Model):
    name = models.CharField(max_length=100, verbose_name="project name")
    description= models.TextField(verbose_name="About project")
    
    def __str__(self):
        return self.name
    
#recent work model

class RecentWork (models.Model):
    title = models.CharField(max_length=100, verbose_name="Work Title")
    image=models.ImageField(upload_to="Works")
    
    def __str__(self):
        return self.title
    

# client model

class skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="client name")
    description = models.TextField(verbose_name="client say")
    image = models.ImageField(upload_to="clients",default="default.png")
    
    def __str__(str):
        return skill.name