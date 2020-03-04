from django.db import models

class Link(models.Model):
    '''
    Model of the links that the user will give
    '''
    
    url = models.URLField()
    access = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.url)