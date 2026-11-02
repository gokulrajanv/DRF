from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self): 
        return f'{self.name} {self.location}'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation=models.CharField(max_length=100)
    image=models.ImageField(upload_to='employee_images/', null=True, blank=True,default='employee_images/default.jpg')
    salary=models.IntegerField()
    joining_date=models.DateField()
    is_active=models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,blank=True)
    manager=models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self): 
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'



# department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,blank=True) 
# this line defines a foreign key relationship between the Employee model and the Department model. 
# This means that each Employee instance is associated with a single Department instance, and 
# the department field in the Employee model will store the primary key of the associated Department instance.

# in short words the department field in the Employee model is a foreign key that references the Department model.
# we using that SET_NULL for when the department is deleted, the foreign key field in the Employee model will be set to null.
# we using that null=True for when the department is not specified, the foreign key field in the Employee model will be set to null.

# media files are the files that are uploaded by the user and we can access them using the url.
# it can be anything that zip file ,pdf file, image file, video file etc. and we can access them using the url.
# an any file that can be uploaded by the user is called as media file and we can access them using the url.


