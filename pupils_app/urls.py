from django.urls import path
from .views import pupils,pupil



urlpatterns=[
    path('pupils/',pupils,name='pupils'),
    path('pupils/<int:pk>/',pupil,name="pupil")



]