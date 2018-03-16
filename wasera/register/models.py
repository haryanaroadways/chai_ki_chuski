from django.db import models
from datetime import date
# Create your models here.
class Owners(models.Model):

    STATES_LIST = (
        ('punjab', 'Punjab'),)

    CITY_LIST = (
    ('jalandhar','Jalandhar'),)

    PARKING_LIST = (
    ('none','None'),
    ('bike','Bike'),
    ('car','Car'),
    ('both','Both'),)

    CC = (
    ('91','+91'),)

    APARTMENT_TYPE = (
    ('apartment','Apartment'),
    ('pg/hostel','PG/Hostel'),
    ('shop','Shop'))

    BHK_TYPE = (
    ('1','1BHK'),
    ('2','2BHK'),
    ('3','3BHK'),
    ('4','4BHK'),
    ('5','4+BHK'),)

    FACING = (
    ('e','East'),
    ('w','West'),
    ('n','North'),
    ('s','South'),
    ('ne','North East'),
    ('nw','North West'),
    ('se','South East'),
    ('sw','South West'),)

    FURNISHING = (
    ('full','Full'),
    ('semi','Semi'),
    ('no','Not Furnished'),)

    PREFFERED_TENANT = (
    ('family','Family'),
    ('bachelor','Bachelor'),
    ('anyone','Anyone'),)



    # fields below
    owners_name = models.CharField(max_length=50,blank=False)
    mail_id = models.EmailField(max_length=100)
    country_code = models.CharField(
        max_length=50,
        choices=CC,
        default='+91',
    )
    phone = models.PositiveIntegerField(blank=False, unique=True)
    apartment_type = models.CharField(
        max_length=50,
        choices=APARTMENT_TYPE)

    bhk_type = models.CharField(
        max_length=50,
        choices=BHK_TYPE,)

    property_size = models.CharField(max_length=150)
    property_age = models.PositiveIntegerField()
    facing = models.CharField(
        max_length=50,
        choices=FACING,)

    rented_floors = models.PositiveIntegerField()
    total_floors = models.PositiveIntegerField()
    expected_rent = models.PositiveIntegerField(default=0)
    negotiable = models.BooleanField(default=False)
    expected_deposit = models.PositiveIntegerField(default=0)
    available_from  = models.DateField(default=date.today)
    furnishing = models.CharField(
        max_length=50,
        choices=FURNISHING,)

    parking = models.CharField(
    max_length=10,
    choices=PARKING_LIST,
    default='none',
    )
    preffered_tenant = models.CharField(
        max_length=50,
        choices=PREFFERED_TENANT,)
        
    address = models.CharField(max_length=500,blank=False,null=False,default='none')
    locality = models.CharField(max_length=200)
    city = models.CharField(
        max_length=50,
        choices=CITY_LIST,
        default='jalandhar',
    )
    pincode = models.PositiveIntegerField()
    state = models.CharField(
        max_length=50,
        choices=STATES_LIST,
        default='punjab',
    )
    property_description = models.TextField()
    owner_pic = models.ImageField(upload_to='owners/%Y/%m/%d/')
