from django.shortcuts import render
from .forms import ImageForm


def upload_image(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.user = request.user
            image.save()
    else:
        image_form = ImageForm()
    return render(request, 'upload.html', {"image_form": image_form})
