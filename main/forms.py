from django import forms
from .models import Employee


class EmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('first_name'), empty_label=None)
