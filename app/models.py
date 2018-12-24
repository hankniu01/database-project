from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    review_count = models.IntegerField()
    yelping_since = models.DateTimeField()
    friends = models.CharField(max_length=100)
    useful = models.IntegerField()
    funny = models.IntegerField()
    cool = models.IntegerField()
    fans = models.IntegerField()
    elite = models.CharField(max_length=50)
    averages_stars = models.FloatField()
    # compliment_hot = models.IntegerField()
    # compliment_profile = models.IntegerField()
    def __str__(self):
        return self.name

class Business(models.Model):
    business_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    stars = models.FloatField()
    review_count = models.IntegerField()
    is_open = models.IntegerField()
    attributes = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    hours = models.DateTimeField()
    def __str__(self):
        return self.name


class Review(models.Model):
    review_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    business_id = models.CharField(max_length=50)
    stars = models.CharField(max_length=50)
    date = models.DateField()
    text = models.TextField()
    # useful = models.IntegerField()
    # funny = models.IntegerField()
    # cool = models.IntegerField()
    def __int__(self):
        return self.review_id

    
