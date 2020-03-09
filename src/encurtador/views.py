from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.dispatch import receiver, Signal
from django.shortcuts import render
from django.urls import reverse
import json

from .models import Link
from .forms import LinkForm

#Signal to get_shortener
request_counter_signal = Signal(providing_args=['link'])

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

            link = Link.objects.order_by('-id')[0]
            short_code = link.to_short_url()

            content = {'link': link.url[:30] + '...', 'short_url': '0.0.0.0:8000/' + short_code, 'short_code': short_code}
            return HttpResponse(json.dumps(content), content_type='encurtador/json')

    context = {'form': form}
    return render(request, 'encurtador/home.html', context)


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
