from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data['title']
        content = serializer.validated_data['content']
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


class ProductListAPIView(generics.RetrieveAPIView):
    """
    not gonna use this
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'