"""
URL configuration for employee_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employee/', include("employees.urls"))
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is for media file 
    # this line is for serving media files in development mode and it will only work when DEBUG is True and it will not work in production mode.

# we make migrations when we make changes or update the models.py file.
# After making migrations, we run migrate to apply those changes to the database.
# if we want to do customization for an admin page we do it in admin.py file.
# include will take destination to the urls.py file of the app.

# path('employee/',include("employee.urls"))
# when an user comes the request with employee , this include will send this request to employee folder in that we hacve the urls.py

#pillow is used for image processing in django. it is a python library for image processing. 