from django.urls import path, include
from django.contrib.auth.views import LogoutView

from bookStore.accounts.views import AppUserLoginView, AppUserRegisterView, ProfileDetailsView, ProfileEditView, \
    ProfileDeleteView

urlpatterns = [
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]