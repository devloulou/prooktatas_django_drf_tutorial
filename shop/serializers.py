from rest_framework import serializers
from .models import GroupCategoryModel, SubCategoryModel, ProductModel


class GroupCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCategoryModel
        fields = ('id', 'category_name', 'description')


class SubCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ('id', 'category', 'sub_category_name', 'sub_category_description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = GroupCategoryModelSerializer(GroupCategoryModel.objects.get(pk=data['category'])).data
        return data


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'product_name', 'price_gross', 'price_net', 'sub_category']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['sub_category'] = SubCategoryModelSerializer(SubCategoryModel.objects.get(pk=data['sub_category'])).data
        return data
