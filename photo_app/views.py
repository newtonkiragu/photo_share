from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ProfileForm, ImageForm


def home(request):

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.poster = request.user
            image.save()
            messages.success(request, 'Your picture has successfully been uploaded.')
    else:
        image_form = ImageForm()
    return render(request, 'home.html', {"image_form": image_form})


@login_required(login_url='/accounts/login/')
def account_edit(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
    else:
        profile_form = ProfileForm()
    return render(request, 'account/edit.html', {"profile_form": profile_form})


@login_required(login_url='/accounts/login/')
def account_profile(request):
    user = request.user
    images = Image.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {"user": user, "images": images})