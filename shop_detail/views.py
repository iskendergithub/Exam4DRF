from django.shortcuts import render
from .serializers import ShopDetailSeriallizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ShopDetail


@api_view(['GET'])
def my_shop_view(request):
    data = {
        'text': 'Welcome'
    }
    return Response(data)


@api_view(['GET'])
def shop_list_view(request):
    shop_list = ShopDetail.objects.all()
    serializer = ShopDetailSeriallizer(shop_list, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def shop_create_view(request):
    serializer = ShopDetailSeriallizer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({"Created: Shop is created !"})


