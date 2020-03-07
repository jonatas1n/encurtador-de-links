from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

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

            link = Link.objects.order_by('id')[0]

            context = {'link': link.url[:30] + '...', 'short_url': '0.0.0.0:8000/' + link.to_short_url()}
            return HttpResponse(context)
    
    context = {'form': form}
    return render(request, 'encurtador/home.html', context)

def get_shortener(request, short_url):
    '''
    Redirect to each site
    '''

    try:
        link = Link.objects.get(pk=Link.to_id(code=short_url))
        link.access += 1
        link.save()
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    return HttpResponseRedirect(link.url)