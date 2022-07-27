from django.db import models


"""
`product_id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(50) NOT NULL,
`quantity_in_stock` int(11) NOT NULL,
`unit_price` decimal(4,2) NOT NULL,
PRIMARY KEY (`product_id`)
"""

# Create your models here.
class Products(models.Model):
	product_id        = models.AutoField(primary_key=True)
	name              = models.CharField(max_length=50, blank=False, null=False)
	quantity_in_stock = models.IntegerField(blank=False, null=False)
	unit_price        = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False)

	class Meta:
		db_table = 'products'
		managed = False # pre-existing table
