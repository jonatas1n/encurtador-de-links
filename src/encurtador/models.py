from django.db import models
import short_url

class Link(models.Model):
    '''
    Model of the links that the user will give
    '''

    url         = models.URLField(null=False)
    access      = models.IntegerField(default=0)
    date_added  = models.DateTimeField(auto_now_add=True)

    def to_id(code):
        return short_url.decode_url(str(code))

    def to_short_url(self):
        return short_url.encode_url(self.id)

    def __str__(self):
        return (self.url + ' : ' + str(self.id))