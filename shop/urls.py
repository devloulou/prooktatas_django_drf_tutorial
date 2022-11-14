from rest_framework import routers
from django.urls import path
from .views import (test_view,
                    test_view2,
                    group_category_view,
                    SubCategoryView,
                    ProductViewset)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'product-viewset', ProductViewset)

urlpatterns = router.urls

urlpatterns += [
    path('test-api/', test_view, name="test-api"),
    path('test-api2/', test_view2, name="test-api2"),
    path('group-category-view/', group_category_view, name="group-category-view"),
    path('sub-category-view/', SubCategoryView.as_view(), name="sub-category-view"),
]