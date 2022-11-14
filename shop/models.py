from django.db import models
from utils.mixins.models import AddDefaultDateColsMixin

"""
category_name	text
description	    text, hosszabb leírást
created_date	automatikusan kapjon értéket insert sorén
modified_date	ő pedig akkor kapjon értéket, amikor egy meglévő adat változik

"""

class GroupCategoryModel(AddDefaultDateColsMixin):
    category_name = models.TextField(max_length=30, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = "group_category"

    def __str__(self):
        return self.category_name

#  lesznek a kategóriáknak alkategóriái

class SubCategoryModel(AddDefaultDateColsMixin):
    category = models.ForeignKey(GroupCategoryModel, on_delete=models.DO_NOTHING)
    sub_category_name = models.CharField(max_length=50, blank=False, null=False)
    sub_category_description = models.TextField(max_length=1500, blank=True, null=True)

    class Meta:
        db_table = "sub_category"

    def __str__(self):
        return self.sub_category_name


class ProductModel(AddDefaultDateColsMixin):
    product_name = models.CharField(null=False, blank=False, max_length=60)
    price_gross = models.IntegerField(null=False, blank=False)
    price_net = models.IntegerField(null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.price_net:
            self.price_net = self.price_gross * 0.73

        super(ProductModel, self).save(*args, **kwargs)