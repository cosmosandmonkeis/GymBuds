from django.shortcuts import render, get_object_or_404
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


# here we can use this list view to list possible user
class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'Search/search-home.html'
    context_object_name = 'UsersList'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'


# here we will use this list view to display specific user's details
class ProfileModifiedListView(ListView):
    model = User
    template_name = 'Search/search-profile-details.html'
    context_object_name = 'specificUser'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Profile.objects.filter(user=user)
