from django.db import models
import short_url

class Link(models.Model):
    '''
    Model of the links that the user will give
    '''

    url         = models.URLField(unique=True, null=False)
    access      = models.IntegerField(default=0)
    date_added  = models.DateTimeField(auto_now_add=True)

    def to_id(code):
        return short_url.decode_url(code)

    def __str__(self):
        return (self.url)