from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'designation', 'image', 'salary', 'joining_date', 'is_active', 'department', 'manager']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}), # used to show the date picker in the form for joining date field
        }

# inside the form we have to pass the meta class and inside the meta class we have to pass the model and fields.
# next we have to render the filds 
# fields ="__all__" - this will render all the fields of the model in the form.