from django.db import models


class CVSection(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    
    def __str__(self):
        return self.title
        
        