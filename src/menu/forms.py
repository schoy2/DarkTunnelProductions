from django import forms
from .models import MenuModel

class EmailCreateForm(forms.Form):
    #name      =forms.CharField()#name field
    email     =forms.CharField()#forms.EmailField()
    about_you = forms.CharField()
    #email  = models.EmailField()
    def clean_name(self):#we created this function to validate names
        name = self.cleaned_data.get("name")
        if name =="Hello":
            raise forms.ValidationError("Not a valid name")
        return name


class MenuModelCreateForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = MenuModel
        fields = ['name','email','about_you']
    def clean_name(self):#we created this function to validate names
        name = self.cleaned_data.get("name")
        if name =="Hello":
            raise forms.ValidationError("Not a valid name")
        return name
