from django import forms


class EmailCreateForm(forms.Form):
    name      =forms.CharField()#name field
    email     =forms.CharField()#forms.EmailField()
    about_you = forms.CharField()
    #email  = models.EmailField()
    def clean_name(self):#we created this function to validate names
        name = self.cleaned_data.get("name")
        if name =="Hello":
            raise forms.ValidationError("Not a valid name")
        return name
