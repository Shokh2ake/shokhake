from django.contrib.auth.models import AbstractUser
from django.db.models import (CASCADE, BooleanField, CharField, DateField,
                              DateTimeField, ForeignKey, ImageField,
                              IntegerField, Model)
from django.db.models.fields import FloatField, TextField
from django_resized import ResizedImageField


class CreateBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(CreateBaseModel):
    name = CharField(max_length=255)


class City(CreateBaseModel):
    name = CharField(max_length=255)
    country = ForeignKey('Country', CASCADE)


class User(AbstractUser):
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users/images',
                              default='media/users/default.jpg')


class Location(CreateBaseModel):
    index = IntegerField()
    city_id = ForeignKey('City', CASCADE)
    description = TextField()


class Courier(CreateBaseModel):
    title = CharField(max_length=255)
    street = CharField(max_length=255)
    building = CharField(max_length=255)
    home_office = CharField(max_length=255)
    index = IntegerField()
    city_id = ForeignKey('City', CASCADE)
    country_id = ForeignKey('Country', CASCADE)
    description = TextField()


class PromoCode(CreateBaseModel):
    name = CharField(max_length=255)
    start_date = DateField()
    end_date = DateField()


class Order(CreateBaseModel):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone_number = CharField(max_length=20)
    email = CharField(max_length=255)
    promo_code = ForeignKey('PromoCode', CASCADE)
    event_id = IntegerField()
    location_id = ForeignKey('Location', CASCADE)
    courier_id = IntegerField()


class Category(CreateBaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=255)


class Venue(CreateBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField()


class Event(CreateBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    start_date = DateField()
    end_date = DateField()
    venues_id = ForeignKey('Venue', CASCADE)
    image = ImageField()
    price = FloatField()
    count = IntegerField()
    city_id = ForeignKey('City', CASCADE)
    category_id = ForeignKey('Category', CASCADE)


class Promotion(CreateBaseModel):
    name = CharField(max_length=255)


class PromotionEvent(CreateBaseModel):
    promotion_id = ForeignKey('Promotion', CASCADE)
    event_id = ForeignKey('Event', CASCADE)


class Session(CreateBaseModel):
    name = CharField(max_length=255)
    start_date = DateField()
    end_date = DateField()
    price = FloatField(default=0)
    event_id = ForeignKey('Event', CASCADE)
    order_id = ForeignKey('Order', CASCADE)


class Like(CreateBaseModel):
    like = IntegerField()
    event_id = ForeignKey('Event', CASCADE)


class Basket(CreateBaseModel):
    count = IntegerField()
    event_id = ForeignKey('Event', CASCADE)
    date_time = DateTimeField()
