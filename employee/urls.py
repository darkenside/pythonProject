from django.urls import path,include
from employee.views import list_employee, create_employee, update_employee, delete_employee

urlpatterns = [
    path('', list_employee, name='list_employee'),
    path('new', create_employee, name='create_employee'),
    path('update/<int:id>/', update_employee, name='update_employee'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
]
