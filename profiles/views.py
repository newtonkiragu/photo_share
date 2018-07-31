from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


def home(request):
    return render(request, 'home.html')


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
    return render(request, 'account/profile.html', {"user": user})
