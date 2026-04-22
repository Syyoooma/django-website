from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,
                  'users/register.html',
                        {'title': 'Registration',
                                'form': form}
                 )

@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        update_user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid() and update_user_form.is_valid():
            profile_form.save()
            update_user_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        profile_form = ProfileImageForm(instance=user_profile)
        update_user_form = UserUpdateForm(instance=request.user)

    data = {
        'profile_form': profile_form,
        'update_user_form': update_user_form,
    }
    return render(request, 'users/profile.html', data)