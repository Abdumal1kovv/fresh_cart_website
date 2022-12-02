from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, ModelForm, IntegerField

from orders.models import Comment, Product


class CustomUserCreationForm(UserCreationForm):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField(max_length=255)


class UserSettingsForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CommentModelForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ('created_at', 'updated_at', 'author')
