from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['category','description', 'deadline', 'priority',]  # Ajoutez 'category' aux champs du formulaire
        widgets = {
            'deadline': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder':  'Ajouter une description'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Sélectionnez une catégorie')]),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
