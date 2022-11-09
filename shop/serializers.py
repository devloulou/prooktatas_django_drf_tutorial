from rest_framework import serializers
from .models import GroupCategoryModel, SubCategoryModel


class GroupCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCategoryModel
        fields = ('id', 'category_name', 'description')


class SubCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ('category', 'sub_category_name', 'sub_category_description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = GroupCategoryModelSerializer(GroupCategoryModel.objects.get(pk=data['category'])).data
        return data
