from django.contrib.auth import logout
from django.shortcuts import render,redirect
from .form import CustomUserCreationForm,UserUpdateForm,ProfileUpdateForm
from .models import ProfileModel
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')

    else:
        form=CustomUserCreationForm()
    context={
        'form':form,
    }
    return render(request,'users/sign_up.html',context)

def custom_logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')  # Or use messages.success for feedback
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)