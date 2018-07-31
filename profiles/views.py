from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


@login_required(login_url='/accounts/login/')
def edit_account(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
    else:
        profile_form = ProfileForm()
    return render(request, 'account/edit.html', {"profile_form": profile_form})
