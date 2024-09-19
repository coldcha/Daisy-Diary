from django.db import models

# Create your models here.

class Date(models.Model):
    """Date for the user when creating a entry."""
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class Entry(models.Model):
    """Entry for the Diary"""
    topic = models.ForeignKey(Date, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}"