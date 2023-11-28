from django import forms
from .models import Investor
from ckeditor.widgets import CKEditorWidget

class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['name', 'email']  # Include other fields as needed

class EmailForm(forms.Form):
    to_email = forms.CharField(
        max_length=256,
    )
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=CKEditorWidget())
    attachment = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)