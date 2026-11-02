from django.shortcuts import render , get_object_or_404 , redirect
from .models import Employee

from .forms import EmployeeForm

# Create your views here.

#decide whiech url pattern to crete 
#created url pattern in the main urls.py and forword to employees.ur;
#created view
#created template

def employee_detail(request,id):
    employee = get_object_or_404(Employee, id=id)
    context = {
        'employee': employee
    }   
    return render(request, 'employee_detail.html', context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES) #request.FILES is used to get the file from the form
        if form.is_valid(): #this will check if the form is valid or not
            form.save()     #this will save the form data to the database
            return redirect('employee_list')  # Redirect to employee list after successful submission
    else:
        form = EmployeeForm() #this the blank employee form that we will render in the template
    return render(request, 'add_employee.html', {'form': form}) #this will render the form in the template

# we using the id to get the employee from the database and pass it to the template
#we can use the id to get the employee

# get_object_or_404 - it will try to get the object based on id and if it is not found it will return a 404 error page.

# query set is the object that has zero or more that came from the ORM that come form data base 
# print(employee) - this the query set

# while printing this we will get the string representation of the object

#     def __str__(self): 
#         return f'{self.first_name} {self.last_name}'

# this is the string representation of the object or model that we will get when we print the object 
