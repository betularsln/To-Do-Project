from django import forms
from .models import Todo

class ListForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["islem_baslik","islem_aciklama","created_on","finished_on","finished"]

        