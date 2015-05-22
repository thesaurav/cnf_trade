from django.db import models
from django.contrib.auth.models import User
#from bid.models import Bid, Bidder
import bid


class AuctionPost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    contact_to_person_name = models.TextField()
    contact_to_person_phone = models.IntegerField()
    cargo_name = models.TextField(max_length=50)
    cargo_quantity = models.IntegerField() # tonnes
    variable_quantity = models.IntegerField() # +/- % in quantity
    category = models.CharField(max_length=30L)
    description = models.CharField(max_length=500L)
    load_port = models.CharField(max_length=50L)
    discharge_port = models.CharField(max_length=50L)
    max_bid_amount = models.FloatField()
    last_bid_rate = models.FloatField()
    last_bid = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    total_bids = models.IntegerField()
    number_of_voyages = models.IntegerField()
    load_rate = models.IntegerField() # per hour
    discharge_rate = models.IntegerField() # per hour
    vessel_type = models.TextField()
    origin_date_from = models.DateTimeField()
    origin_date_to = models.DateTimeField()
    destination_date_from = models.DateTimeField()
    destination_date_to = models.DateTimeField()
    other_requirements = models.TextField(max_length=1000) # includes cumpolsory requirements
    terms_conditions = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    in_deal_phase = models.BooleanField(default=False)
    confirmation_period = models.IntegerField() # hours / days
    deal_successful = models.BooleanField(default=False)
    grace_confirmation_period = models.IntegerField(default=0)





class Auctioneer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    phone_number = models.IntegerField()
    fax = models.IntegerField()
    is_dnd = models.BooleanField()
    country = models.TextField(max_length=100)
    state = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    pin_code = models.IntegerField()
    registered_address = models.TextField(max_length=100)
    total_posts = models.IntegerField()
    is_privileged = models.BooleanField(False)
    email1 = models.EmailField()
    business_activity = models.TextField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    organisation_name = models.TextField(max_length=100)
    organisation_type = models.TextField(max_length=100)
    contact_person = models.TextField(max_length=100)
    designation = models.TextField()

class AuctioneerNotification(models.Model):
    id = models.AutoField(primary_key=True)
    auction_id = models.ForeignKey(AuctionPost)
    bid_id = models.ForeignKey('bid.Bid')
    auctioneer_id = models.ForeignKey(Auctioneer)
    bidder_id = models.ForeignKey('bid.Bidder')
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    message = models.TextField(max_length=2000L)
