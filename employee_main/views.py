from django.http import HttpResponse
from employees.models import Employee
from django.shortcuts import render



def home(request):
    #fetching data form employee model
    employees = Employee.objects.all()
    context={
        'employees':employees
    }
    return render(request,'home.html',context)




#  employees = Employee.objects.all() - this bring all the data form the employee model and it will store in employees variable
# query set is an object that contains the result of the database query-zero or more recodres 
# in django any data comes from the database is known as query set
# the render function is used to render the html page and pass the data to the html page
#the render function alwasys take the request as the first argument and 
# the html page as the second argument and the data as the third argument
# we using the context variable to pass the data to the html page
