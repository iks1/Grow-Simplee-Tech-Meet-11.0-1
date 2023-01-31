from django.db import models
from django.utils.translation import gettext_lazy as _
from .choices import *
import os


# Create your models here.

class Manager(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=500, null=True)
    address_id = models.CharField(max_length=500)

    def __str__(self):
        return self.name + self.id

class Address(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
<<<<<<< HEAD
    latitude = models.CharField(max_length=50, default='')
    longitude = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=250, default='')
    name = models.CharField(max_length=50, default='')
=======
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
<<<<<<< HEAD
>>>>>>> f2debc68cd74c014357b7358f0b611b2d194d036
=======
>>>>>>> 3e3d68a7838231ef1fe9581eb3ec7131ec588df2
    def __str__(self):
        return f"Address-{self.location}"

class Rider(models.Model):
    name = models.CharField(max_length=250, default='')
    rider_id = models.CharField(max_length=500, default='')
    contact_number = models.CharField(max_length=10, default='')
    bag_volume = models.CharField(max_length=50, default='')
    bag_volume_used = models.CharField(max_length=50, default='')
    current_address = models.ForeignKey(
        Address, related_name="Current_Delievery_Address", on_delete=models.CASCADE
    )
    rider_status = models.CharField(
        _("filing form type"), max_length=50, choices=RIDER_STATUS
    )
    # delievery_orders = models.ManyToManyField(
    #     Order, related_name="Orders_Assigned", blank=True
    # )
    last_delivered_pointer = models.IntegerField(default=0)
    manager_id = models.CharField(max_length=500)
    arrival_time = models.DateField((_("arrival time")))
    departure_time = models.DateField((_("departure time")))
    etf = models.CharField(max_length=50, default='')
    successful_deliveries = models.IntegerField(default=0)
    packages_delayed = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.successful_deliveries = self.last_delivered_pointer + 1
        self.packages_delayed = 0
        for order in self.delievery_orders:
            if order.order_status == "delayed":
                self.packages_delayed += 1
        super(Rider, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} + {self.rider_id}"

class Owner(models.Model):
    owner_id = models.CharField(max_length=500)
    name = models.CharField(max_length=500, null=True)
    contact_number = models.CharField(max_length=500, null=True)
    address_id = models.CharField(max_length=500)

    def __str__(self):
        return self.name + self.address_id


<<<<<<< HEAD
<<<<<<< HEAD
class Order(models.Model):
    # rider_id = models.CharField(max_length=500)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, blank=True, null=True)
=======
=======
>>>>>>> 3e3d68a7838231ef1fe9581eb3ec7131ec588df2
class Rider(models.Model):
    name = models.CharField(max_length=250)
    rider_id = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=10)
    bag_volume = models.CharField(max_length=50)
    bag_volume_used = models.CharField(max_length=50)
    current_address = models.ForeignKey(
        Address, related_name="Current_Delievery_Address", on_delete=models.CASCADE
    )
    rider_status = models.CharField(
        _("filing form type"), max_length=50, choices=RIDER_STATUS
    )
    delievery_orders = models.CharField(max_length=500)
    last_delivered_pointer = models.IntegerField()
    manager_id = models.CharField(max_length=500)
    arrival_time = models.DateField((_("arrival time")))
    departure_time = models.DateField((_("departure time")))
    etf = models.CharField(max_length=50)
    successful_deliveries = models.IntegerField(default=0)
    packages_delayed = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # self.successful_deliveries = self.last_delivered_pointer + 1
        # self.packages_delayed = 0
        # for order_id in self.delievery_orders.split(","):
        #     if Order.objects.get(id=order_id).order_status == "delayed":
        #         self.packages_delayed += 1
        super(Rider, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} + {self.rider_id}"

class Order(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
>>>>>>> f2debc68cd74c014357b7358f0b611b2d194d036
    order_name = models.CharField(max_length=500, null=True, blank=True)
    shape = models.CharField(max_length=50, null=True, blank=True)
    volume = models.CharField(max_length=50, blank=True)
    length = models.CharField(max_length=50, blank=True)
    width = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
<<<<<<< HEAD
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    # address_id = models.CharField(max_length=500, blank=True)
    delivery_action = models.CharField(
        _("delivery action"), max_length=50, choices=DELIVERY_ACTION, blank=True
    )
    in_warehouse = models.BooleanField(default=False, null=True)
    order_status = models.CharField(
        _("order status"), max_length=50, choices=ORDER_STATUS, blank=True
    )
    edd = models.DateField(_("EDD date"), blank=True, null=True)
    eta = models.CharField(max_length=50, null=True)
=======
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    delivery_action = models.CharField(
        _("delivery action"), max_length=50, choices=DELIVERY_ACTION, blank=True
    )
    order_status = models.CharField(
        _("order status"), max_length=50, choices=ORDER_STATUS, blank=True
    )
    edd = models.DateTimeField(_("EDD date"), blank=True, null=True)
    eta = models.CharField(max_length=50)
>>>>>>> f2debc68cd74c014357b7358f0b611b2d194d036
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.order_name
    
class Bags(models.Model):
    rider_id = models.CharField(max_length=500)
    order_name = models.CharField(max_length=500, null=True, blank=True)
    shape = models.CharField(max_length=50, null=True, blank=True)
    volume = models.CharField(max_length=50, blank=True)
    length = models.CharField(max_length=50, blank=True)
    width = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.order_name

class Repository(models.Model):
    cancelled = models.IntegerField(default=0)
    pickups = models.IntegerField(default=0)
    damaged = models.IntegerField(default=0)
    history = models.TextField()

    def __str__(self):
        return f"Repository"

def get_upload_to(instance, filename):
    return os.path.join("media/", str(instance.order.order_name), filename)

class OrderImage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    images = models.FileField(upload_to=get_upload_to, blank=True)

class RiderRewards(models.Model):
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    rider_name = models.CharField(max_length=100, blank=True, null=True)
    successful_deliveries = models.IntegerField(blank=True, null=True)
    earnings = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return {self.rider_name} + "RiderRewards"
