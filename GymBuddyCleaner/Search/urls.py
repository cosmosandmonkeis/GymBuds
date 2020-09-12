from django.urls import path, include
from . import views
from .views import ProfileListView, ProfileModifiedListView

urlpatterns = [
    path('', ProfileListView.as_view(), name='search-home'),
    path('user/<str:username>', ProfileModifiedListView.as_view(), name='profile-detail')
    # path('', views.home, name='search-home'),
]