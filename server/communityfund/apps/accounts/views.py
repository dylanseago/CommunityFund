from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from communityfund.apps.home import views as HomeViews
from communityfund.apps.accounts.forms import SignupForm


@login_required
def profile(request):
    # TODO change to use a profile page instead
    return HomeViews.user(request, request.user.id)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form
    })