from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'Search/search-home.html', {})

def nonauth_home(request):
    return render(request, 'Search/nonauth-home.html', {})