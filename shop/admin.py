from django.contrib import admin
from .models import GroupCategoryModel, SubCategoryModel, ProductModel

admin.site.register(GroupCategoryModel)
admin.site.register(SubCategoryModel)
admin.site.register(ProductModel)