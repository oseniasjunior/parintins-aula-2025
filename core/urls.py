from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register('employee', viewsets.EmployeeViewSet)

urlpatterns = router.urls
