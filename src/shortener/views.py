from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.dispatch import receiver, Signal
from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse
import logging
import json

from .models import Link
from .forms import LinkForm

#Signal to get_shortener
request_counter_signal  = Signal(providing_args=['link'])
log                     = logging.getLogger()

def new_link(request):
    '''
    Site's Home page, in home page the user will be possible to create a shortened link
    '''

    if request.method != 'POST':
        form = LinkForm()
    else:
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse(json.dumps(create_content()), content_type='shortener/json')

    context = {'form': form}
    return render(request, 'shortener/home.html', context)


def create_content():
    link = Link.objects.latest('id')
    short_code = link.to_short_url()

    content = {'link': link.url[:30] + '...', 'short_url': '0.0.0.0:8000/' + short_code, 'short_code': short_code}
            
    return content


def get_shortener(request, short_url):
    '''
    Redirect to each site
    '''

    try:
        code_id = Link.to_id(short_url)
        link = Link.objects.get(pk=code_id)

        request_counter_signal.send(sender = Link, link = link)
    
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    return HttpResponseRedirect(link.url)


@receiver(request_counter_signal)
def set_access_count(sender, **kwargs):
    '''
    Add 1 in access url
    '''

    kwargs['link'].access += 1
    kwargs['link'].save()


def get_url_rank(request):
    '''
    Return the rank to home page
    '''
    
    return render(request, 'shortener/rank.html', create_context())

def create_context():

    urls = Link.objects.values('url').order_by().annotate(Sum('access'))
    context = {'urls': urls.order_by('-access__sum')[:5]}
          
    return context