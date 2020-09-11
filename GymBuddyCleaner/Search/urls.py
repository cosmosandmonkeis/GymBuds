from django.urls import path, include
from . import views
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', ProfileListView.as_view(), name='search-home'),
    path('<str:user>', ProfileDetailView.as_view(), name='profile-detail')
    # path('', views.home, name='search-home'),
]