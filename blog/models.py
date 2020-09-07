from django.db import models
from jobs.models import Job

# Create a blog model
# Title
# Publication date
# Body - text
# Image connected to post

class Blog(models.Model):
    # Title
    title = models.CharField(max_length=100)
    # Publication date
    pub_date = models.DateTimeField()
    # Body - text
    body = models.TextField()
    # Image connected to post
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title 

    def summary(self):
        return self.body[0:100]


    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
# Add Blog app to settings - go to settings file and insert under apps 
# create a migration - python manage.py makemigrations
# Migrate - python manage.py migrate

# add to the admin
