
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from .models import ariza
from django.forms import ModelForm, forms

# class authentificatemodelform(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class loginmodelform(AuthenticationForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)

    


# class AdminModelForm(ModelForm):
#     class Meta:
#         model = admin
#         fields = ['name', 'price', 'contains_sugar', 'image']






class ArizaModelFoem(ModelForm):

    class Meta:
        model = ariza
        fields = ['kimga', 'qisqacha_shikoyat_matni']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user

        if commit:
            instance.save()

        return instance
