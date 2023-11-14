from django.db import models


# Create your models here.
class Booking(models.Model):
    #id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.SmallIntegerField(null=False)
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        if self.number_of_guests == 1:
            return f'{self.name} for {self.number_of_guests} guest on {self.booking_date}'
        else:
            return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'



# Add code to create Menu model
class Menu(models.Model):
   #id = models.IntegerField(default=1,primary_key=True)
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10,decimal_places=2) 
   inventory = models.IntegerField(null=False) 

   def __str__(self) -> str: 
       return f'{self.title} : {str(self.price)}'
   