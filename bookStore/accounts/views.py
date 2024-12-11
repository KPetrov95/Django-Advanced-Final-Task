from django.contrib import messages
from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, View

from bookStore.accounts.forms import ProfileEditForm, AppUserCreationForm
from bookStore.accounts.models import UserProfile, AppUser

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('book_list')


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    pk_url_kwarg = 'pk'


class ProfileDeleteView(LoginRequiredMixin, View):
    model = AppUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(AppUser, pk=kwargs['pk'])
        return render(request, self.template_name, {'user': user})

    def post(self, request, *args, **kwargs):
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        messages.success(request, "Your account has been deactivated. You can no longer log in.")
        return HttpResponseRedirect(self.success_url)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def test_func(self):
        profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )
