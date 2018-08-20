from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;width: 705px;'}),
        help_text = 'Insira ou Atualize o email aqui!',

    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'style': 'border-color: orange;width: 705px;'}),
        help_text='Insira ou Atualize o nome aqui!',
    )

    department = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'style': 'border-color: orange;width: 705px;'}),
        help_text='Insira ou Atualize o departamento aqui!',
    )