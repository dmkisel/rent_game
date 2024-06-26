from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser

class RegisretForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'name', 'telegram', 'password1', 'password2')


class ProfileForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = '__all__'

