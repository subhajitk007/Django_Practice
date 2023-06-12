from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('all_employee', views.all_employee, name='all_employee'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('rem_employee', views.rem_employee, name='rem_employee'),
    path('rem_employee/<int:emp_id>', views.rem_employee, name='rem_employee'),
    path('filter_employee', views.filter_employee, name='filter_employee'),
]