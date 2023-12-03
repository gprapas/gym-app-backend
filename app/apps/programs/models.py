from django.db import models

class GymFile(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Gym Programs'

    
