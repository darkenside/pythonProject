
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from employee.sets import EmployeeViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'employee',EmployeeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/',include('employee.urls')),
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls'))
]
