from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# from django.http import Http404

""" 
    generics are more readable@! 
"""


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data['title']
        content = serializer.validated_data.get('content', None)  # safe
        # or None
        # if title is None:
        #     raise serializers.ValidationError("Title is required")
        if content is None:
            content = title
            # raise serializers.ValidationError("Content is required")
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title
            # instance.save()   don't save


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.ListModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Product.objects.all()
#     serializer = ProductSerializer
#     lookup_field = 'pk'
#
#     def get(self, request, *args, **kwargs):  # HTTP -> get
#         # return self.list(request, *args, **kwargs)
#         # return Response({"message": "GET METHOD"})
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)  # queryset
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     # def perform_create(self, serializer):
#     #     title = serializer.validated_data['title']
#     #     content = serializer.validated_data.get('content', None)
#     #     if content is None:
#     #         content = "this is a single view doing cool stuff"
#     # (... not finished)




# class ProductListAPIView(generics.ListAPIView):
#     """
#     not gonna use this method because ProductListCreateAPIView will do the same *almost*
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'


# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#
#     if method == "GET":
#
#         if pk is not None:
#             """detailed view"""
#
#             queryset = Product.objects.filter(pk=pk)
#             obj = get_object_or_404(queryset, pk=pk)
#
#             # if not queryset.exists():
#             #     # return Response({"message": "Not found"}, status=404)
#             #     raise Http404
#
#             data = ProductSerializer(obj, many=False).data
#             return Response()
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)
#
#     if method == "POST":
#
#         serializer = ProductSerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#
#             title = serializer.validated_data['title']
#             content = serializer.validated_data.get('content', None)
#
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=400)
