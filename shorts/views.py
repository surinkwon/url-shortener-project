import string
import random
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe
from .models import ShortUrl
from .forms import ShortUrlForm, CustomShortUrlForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def shortening(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            origin_url = form.save(commit=False)
            new_url = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(7)])
            while ShortUrl.objects.filter(url_name=new_url).exists():
                new_url = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(7)])
            origin_url.url_name = new_url
            origin_url.save()
            context = {
                'submited': 1,
                'new_url': 'http://127.0.0.1:8000/' + new_url,
            }
            return render(request, 'shorts/shorten.html', context)
    else:
        form = ShortUrlForm()
    context = {
        'submited': 0,
        'form': form,
    }
    return render(request, 'shorts/shorten.html', context)


@require_http_methods(['GET', 'POST'])
def custom_shortening(request):
    if request.method == 'POST':
        form = CustomShortUrlForm(request.POST)
        if form.is_valid():
            new_url = form.save()
            custom_string = new_url.url_name
            context = {
                'submited': 1,
                'new_url': 'http://127.0.0.1:8000/' + custom_string,
            }
            return render(request, 'shorts/customshorten.html', context)
    else:
        form = CustomShortUrlForm()
    context = {
        'submited': 0,
        'form': form,
    }
    return render(request, 'shorts/customshorten.html', context)


@require_safe
def connect_to_original(request, new_url):
    urlname = ShortUrl.objects.get(url_name=new_url)
    origin_url = urlname.original_url
    print(origin_url)
    return redirect(origin_url)
