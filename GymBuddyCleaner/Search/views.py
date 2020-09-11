from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from Users.models import Profile

# Create your views here.


@login_required
def home(request):
    return render(request, 'Search/search-home.html', {})


def nonauth_home(request):
    return render(request, 'Search/nonauth-home.html', {})


class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'Search/search-home.html'
    context_object_name = 'UsersList'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'Search/search-profile-details.html'

    slug_field = 'user'
    slug_url_kwarg = 'user'
