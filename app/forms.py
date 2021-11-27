from django import forms
from app.models import Count

class CountForm(forms.ModelForm):
    class Meta:
        model = Count
        fields = "__all__"

    