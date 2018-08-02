from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from friendship.models import Follow
from .models import Image, Comment
from .forms import ProfileForm, ImageForm, CommentForm


def home(request):
    images = Image.objects.all()
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request, 'home.html', {"images": images, "comments": comments, "form": form})


@login_required
def image_comment(request, id):
    image = Image.objects.get(id=id)
    comments = Comment.objects.filter(image_id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.image_id = image.id
            comment.save()
            messages.success(request, 'Your comment has been posted.')
    else:
        form = CommentForm()
    return redirect('home')


@login_required
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


@login_required
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


@login_required
def account_profile(request):
    user = request.user
    followers = Follow.objects.followers(request.user)
    following = Follow.objects.following(request.user)
    images = Image.objects.filter(poster=user)
    followers_number = len(followers)
    following_number = len(following)
    images_number = len(images)
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted.')
    else:
        form = CommentForm()

    return render(request, 'account/profile.html', {"user": user, "images": images, "followers": followers,
                                                    "following": following, "followers_number": followers_number,
                                                    "following_number": following_number, "form": form,
                                                    "comments":comments, "images_number": images_number})


def user_profile(request, username):
    user = User.objects.get(username=username)
    followers = Follow.objects.followers(user)
    following = Follow.objects.following(user)
    images = Image.objects.filter(poster=user)
    followers_number = len(followers)
    following_number = len(following)
    images_number = len(images)
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted.')
    else:
        form = CommentForm()

    return render(request, 'account/profile.html', {"user": user, "images": images, "followers": followers,
                                                    "following": following, "followers_number": followers_number,
                                                    "following_number": following_number, "form": form,
                                                    "comments": comments, "images_number": images_number})


@login_required(login_url='/accounts/login/')
def follow_user(request, username):
    other_user = User.objects.get(username=username)
    Follow.objects.add_follower(request.user, other_user)
    return redirect('user_profile', username=username)


@login_required(login_url='/accounts/login/')
def unfollow_user(request, username):
    other_user = User.objects.get(username=username)
    Follow.objects.remove_follower(request.user, other_user)
    return redirect('user_profile', username=username)