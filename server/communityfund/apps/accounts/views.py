from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from communityfund.apps.home import views as HomeViews


@login_required
def profile(request):
    return HomeViews.user(request, 0)