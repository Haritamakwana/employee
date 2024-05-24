from django import forms
from myapp.models import employee

class empform(forms.ModelForm):
    class Meta:
        model=employee
        fields=["ename","eemail","econtact"]