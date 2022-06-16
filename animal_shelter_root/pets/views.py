from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Pet
from .forms import ImageUploadForm


def index(request):
    data = Pet.objects.all()
    context = {
        'data': data
    }
    return render(request, 'pets/display.html', context)


def uploadView(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageUploadForm()
    return render(request, 'pets/upload.html', {'form': form})
