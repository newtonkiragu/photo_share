from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from friendship.models import Follow
from .models import Image
from .forms import ProfileForm, ImageForm


def home(request):

    return render(request, 'home.html',)


def image_post(request):

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.poster = request.user
            image.save()
            messages.success(request, 'Your picture has successfully been uploaded.')
    else:
        image_form = ImageForm()
    return render(request, 'image_post.html', {"image_form": image_form})


@login_required(login_url='/accounts/login/')
def account_edit(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been updated.')
    else:
        profile_form = ProfileForm()
    return render(request, 'account/edit.html', {"profile_form": profile_form})


@login_required(login_url='/accounts/login/')
def account_profile(request):
    user = request.user
    followers = Follow.objects.followers(request.user)
    following = Follow.objects.followers(request.user)
    followers_number = len(followers)
    following_number = len(following)
    images = Image.objects.filter(poster=user)
    return render(request, 'account/profile.html', {"user": user, "images": images, "followers": followers,
                                                    "following": following, "followers_number": followers_number,
                                                    "following_number": following_number})


def user_profile(request, username):
    user = User.objects.get(username=username)
    images = Image.objects.filter(poster=user)
    return render(request, 'account/profile.html', {"user": user, "images": images})


@login_required(login_url='/accounts/login/')
def follow_user(request, username):
    other_user = User.objects.get(username=username)
    Follow.objects.add_follower(request.user, other_user)
    return render(request, '')
