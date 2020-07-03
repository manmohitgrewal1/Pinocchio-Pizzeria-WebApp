from django.db import models

# Create your models here.
class RegularPizza(models.Model):
    item= models.CharField(max_length=50)
    large= models.FloatField(max_length=20)
    small= models.FloatField(max_length=20)


    def __str__(self):
        return f"{self.item}"

class SicilianPizza(models.Model):
    item= models.CharField(max_length=50)
    large= models.FloatField(max_length=20)
    small= models.FloatField(max_length=20)


    def __str__(self):
        return f"{self.item}"

class Pasta(models.Model):
    item= models.CharField(max_length=50)
    price= models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.item}"

class Salad(models.Model):
    item= models.CharField(max_length=50)
    price= models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.item}"
    
class Subs(models.Model):
    item= models.CharField(max_length=50)
    large= models.FloatField(max_length=20)
    small= models.FloatField(max_length=20)


    def __str__(self):
        return f"{self.item}"

class DinnerPlatter(models.Model):
    item= models.CharField(max_length=50)
    large=models.FloatField(max_length=20)
    small= models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.item}"

class Topping(models.Model):
    item=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.item}"

class SubTopping(models.Model):
    item=models.CharField(max_length=50)
    large=models.FloatField(max_length=20)
    small= models.FloatField(max_length=20)
    
    def __str__(self):
        return f"{self.item}"

class User(models.Model):
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)

    def __str__(self):
        return self.username
    

class Order(models.Model):
    ORDER_STATUS= (('P', 'Pending'), ('C', 'Confirmed'))
    item= models.CharField(default= '!Add an item!', max_length=50)
    varient= models.CharField( default= '!Add an varient!',max_length=50)
    topping= models.ManyToManyField(Topping, blank=True, related_name='order')
    sub_topping= models.ManyToManyField(SubTopping, blank=True, related_name='order')
    amount=models.FloatField(default= '0')
    user= models.ManyToManyField(User, related_name='order')
    size= models.CharField(default= '-', max_length=50)
    status= models.CharField(max_length=1, default="P", choices= ORDER_STATUS)
    
    def __str__(self):
        return self.item

    def get_user(self):
        return "\n".join([str(u) for u in self.user.all()])

    def get_topping(self):
        return "\n".join([str(u) for u in self.topping.all()])