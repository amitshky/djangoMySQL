from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, permissions

from .models import Products
from .serializers import ProductsSerializer


### Function-based API Views ###
@api_view(['GET'])
def getProducts(req: Request):
	queryset = Products.objects.all()
	serializer = ProductsSerializer(queryset, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def getProductDetails(req: Request, pk: int):
	try:
		queryset: Products = Products.objects.get(product_id=pk)
	except Products.DoesNotExist:
		return Response({ 'error': 'This item doesn\'t exist.' })

	serializer = ProductsSerializer(queryset)
	return Response(serializer.data)


@api_view(['POST'])
def addProduct(req: Request):
	serializer = ProductsSerializer(data=req.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	
	return Response({ 'error': 'Invalid data!' }, status=400)


@api_view(['PUT'])
def updateProduct(req: Request, pk: int):
	queryset: Products = Products.objects.get(product_id=pk)
	serializer = ProductsSerializer(instance=queryset, data=req.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	
	return Response({ 'error': 'Invalid data!' }, status=400)


@api_view(['DELETE'])
def deleteProduct(req: Request, pk: int):
	try:
		queryset: Products = Products.objects.get(product_id=pk)
	except Products.DoesNotExist:
		return Response({ 'error': 'This item doesn\'t exist.' })

	
	queryset.delete()
	return Response({'message': 'Product deleted successfully!'})


### Class-based API Views ###
# read
class ProductDetailAPIView(generics.RetrieveAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductsSerializer
	lookup_field = 'pk'


# read and create
class ProductListCreateAPIView(generics.ListCreateAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductsSerializer
	lookup_field = 'pk'

	def perform_create(self, serializer):
		serializer.save()


# update
class ProductUpdateAPIView(generics.UpdateAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductsSerializer
	lookup_field = 'pk'

	def perform_update(self, serializer):
		serializer.save()


# delete
class ProductDestroyAPIView(generics.DestroyAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductsSerializer
	lookup_field = 'pk'

	def perform_destroy(self, instance):
		return super().perform_destroy(instance)


### Mixins ###
class ProductMixinView(
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	mixins.CreateModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIView # for .as_view() in urls.py
):
	queryset = Products.objects.all()
	serializer_class = ProductsSerializer
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	lookup_field = 'pk'

	def get(self, req: Request, *args, **kwargs):
		pk = kwargs.get('pk')
		if pk != None:
			return self.retrieve(req, *args, **kwargs)
		return self.list(req, *args, **kwargs)


	def post(self, req: Request, *args, **kwargs):
		return self.create(req, *args, **kwargs)


	def put(self, req: Request, *args, **kwargs):
		return self.update(req, *args, **kwargs)


	def delete(self, req: Request, *args, **kwargs):
		return self.destroy(req, *args, **kwargs)