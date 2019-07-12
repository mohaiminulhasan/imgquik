import hashlib

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import etag

from .forms import ImageForm

def home(request):
    return render(request, "home.html")

def generate_etag(request, width, height, bg=None, fg=None):
    content = 'Placeholder: {0} x {1} BG: {2} FG: {3}'.format(width, height, bg, fg)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)
def generate_image(request, width, height, bg='000000', fg='FFFFFF'):
    form = ImageForm({'width': width, 'height': height})
    if form.is_valid():
        image = form.generate(bg='#{}'.format(bg), fg='#{}'.format(fg))
        return HttpResponse(image, content_type='image/png')
    else:
        return  HttpResponseBadRequest('Invalid Image Request')