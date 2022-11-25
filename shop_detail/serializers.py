from rest_framework import serializers
from .models import ShopDetail


class ShopDetailSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetail
        fields = '__all__'