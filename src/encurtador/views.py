from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import json

from .models import Link
from .forms import LinkForm

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
        link = Link.objects.get(pk=Link.to_id(short_url))
        link.access += 1
        link.save()
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    return HttpResponseRedirect(link.url)