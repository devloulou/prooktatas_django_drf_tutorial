from django.contrib import admin
from .models import GroupCategoryModel, SubCategoryModel

admin.site.register(GroupCategoryModel)
admin.site.register(SubCategoryModel)