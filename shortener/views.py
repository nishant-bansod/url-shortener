# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import URLForm
from .models import ShortURL

def home(request):
    form = URLForm()
    short_url = None

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_obj = form.save()
            short_url = request.build_absolute_uri('/') + url_obj.short_code

    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})


def redirect_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    return redirect(url.original_url)
