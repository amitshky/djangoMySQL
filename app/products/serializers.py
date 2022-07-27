from rest_framework import serializers

from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
	name              = serializers.CharField(max_length=50, required=True)
	quantity_in_stock = serializers.IntegerField(required=True)
	unit_price        = serializers.DecimalField(max_digits=4, decimal_places=2, required=True)

	class Meta:
		model = Products
		# specify fields you want to serialize
		fields = ['product_id', 'name', 'quantity_in_stock', 'unit_price']

