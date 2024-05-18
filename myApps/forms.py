from django import forms
from .models import PasswordManager,FormTest



class BlogForm(forms.ModelForm):
    class Meta:
        model = FormTest
        fields=['postname','postbody','slug']