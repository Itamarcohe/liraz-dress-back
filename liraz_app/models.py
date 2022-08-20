from django.db import models

class MetaModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Dress(MetaModel):
    dress_name = models.CharField(max_length=512, null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    description = models.CharField(max_length=1028,null=True,blank=True)
    image = models.URLField(max_length=512)
    size=  models.CharField(max_length=128,null=True,blank=True)
    featured_image = models.URLField(max_length=512, default='https://cdn1.bambinifashion.com/img/p/6/4/9/4/0/8/649408--product-gallery.jpg')

    def __str__(self):
        return self.dress_name


class Lead(MetaModel):
    full_name = models.CharField(max_length=512, null=False,blank=False)
    phone_number = models.CharField(max_length=15,null=False,blank=False)
    email = models.EmailField()
    description = models.CharField(max_length=2048,null=False,blank=False)

    def __str__(self):
        return f"{self.full_name} Lead at {self.created_at}"


class Order(MetaModel):
    customer_name = models.CharField(max_length=512,null=False,blank=False)
    phone_number = models.CharField(max_length=128,null=False,blank=False)
    top_item = models.IntegerField(null=False,blank=False)
    back_item = models.IntegerField(null=False,blank=False)
    bottom_item = models.IntegerField(null=False,blank=False)
    color = models.CharField(max_length=128,null=True,blank=True)


# Create your models here.
