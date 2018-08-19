from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from django.shortcuts import render


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer