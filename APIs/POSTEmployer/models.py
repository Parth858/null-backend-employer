from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # Add more feilds as per your requirements.

    def __str__(self):
        return self.title