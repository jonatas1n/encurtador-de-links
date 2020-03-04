from django.shortcuts import render

from .models import Link

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
            return HttpResponseRedirect(reverse('encurtador:new_link'))
    
    context = {'form': form}
    return render(request, 'encurtador/home.html', context)

