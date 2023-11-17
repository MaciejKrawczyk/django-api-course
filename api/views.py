from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF api view
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        # print(serializer.data)
        return Response(serializer.data)


    # instance = Product.objects.order_by("?").first()
    # data = {}
    #
    # if instance:
    #     # data['id'] = model_data.id
    #     # data["title"] = model_data.title
    #     # data["content"] = model_data.content
    #     # data['price'] = model_data.price
    #
    #     data = ProductSerializer(instance).data
    #
    #     # data = model_to_dict(model_data, fields=["id", "title", "price", "sale_price"])
    #
    #     # json_data_str = json.dumps(data)
    #
    #     # model instance (model_data)
    #     # turn a python dict
    #     # return json to my client
    #     # serialization

    # return JsonResponse(data)

    # return JsonResponse(data)
