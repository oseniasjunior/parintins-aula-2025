from rest_framework import routers

from cruds import viewsets

router = routers.DefaultRouter()
router.register('marital_status', viewsets.MaritalStatusViewSet)
router.register('department', viewsets.DepartmentViewSet)
router.register('product_group', viewsets.ProductGroupViewSet)
router.register('supplier', viewsets.SupplierGroupViewSet)
router.register('product', viewsets.ProductViewSet)

urlpatterns = router.urls
