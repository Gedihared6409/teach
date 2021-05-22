from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	CATEG = (
		('HIRE','HIRE'),
		('WORK','WORK'),
	)
	user = models.OneToOneField(User, null=True, blank = True ,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	catego = models.CharField(max_length=200, null=True, choices=CATEG)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField( default='DSC_0002.JPG', null = True , blank = True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.name)

class repairAsset(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    AssetName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    reason = models.TextField(max_length=200)
    urgent = models.CharField(max_length=200)
    

    def __str__(self):
        return str(self.customer)

    def save_repair(self):
        self.save()
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.name)
class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return str(self.name)

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return str(self.note)

	# def __str__(self):
	# 	return str(self.product)