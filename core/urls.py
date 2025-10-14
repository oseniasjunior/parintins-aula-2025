from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register('employee', viewsets.EmployeeViewSet)
router.register('customer', viewsets.CustomerViewSet)
router.register('branch', viewsets.BranchViewSet)
router.register('sale', viewsets.SaleViewSet)
router.register('sale_item', viewsets.SaleItemViewSet)

urlpatterns = router.urls
