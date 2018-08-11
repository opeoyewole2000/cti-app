from django import forms
from .models import ctiRawTable


class clfFileForm(forms.ModelForm):
    class Meta:
        model = ctiRawTable
        fields = [
            # "file_upload",
        ]