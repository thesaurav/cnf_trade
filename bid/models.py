from django.contrib.auth.models import User
from django.db import models
from auction.models import AuctionPost, Auctioneer
from bid.choices import YEARS

# Create your models here.

#class b_authUser(models.Model):
#    id = models.IntegerField(primary_key=True)
#    username = models.CharField(max_length=60L, unique=True, blank=True)
#    first_name = models.CharField(max_length=30L)
#    last_name = models.CharField(max_length=30L)
#    email = models.CharField(max_length=75L)
#    password = models.CharField(max_length=128L)
#    is_staff = models.IntegerField()
#    is_active = models.IntegerField()
#    is_superuser = models.IntegerField()
#    last_login = models.DateTimeField()
#    date_joined = models.DateTimeField()
#    class Meta:
#        db_table = 'auth_user'
#        app_label = 'bidder'
class Bidder(models.Model):
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
    is_privileged = models.BooleanField(default=False)
    email1 = models.EmailField()
    business_activity = models.TextField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    organisation_name = models.TextField(max_length=100)
    organisation_type = models.TextField(max_length=100)
    contact_person = models.TextField(max_length=100)
    designation = models.TextField()
    total_bids_made = models.IntegerField()

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Bidder)
    auction_id = models.ForeignKey(AuctionPost)
    contact_to_person_phone = models.IntegerField()
    contact_to_person_name = models.TextField(max_length=50,default=None) #Name
    bid_time = models.DateTimeField(auto_now=True)
    bid_price = models.FloatField()
    bid_comment = models.TextField(max_length=255)
    expected_voyage_start_date = models.DateTimeField(default=None)
    origin = models.TextField(max_length=100)
    destination = models.TextField(max_length=100)
    vessel = models.ForeignKey('Vessel')
    terms_conditions = models.TextField(max_length=1000)
    accepted_terms = models.TextField()
    in_deal_phase = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_halted = models.BooleanField(default=False)
    expected_voyage_end_date = models.DateTimeField()
    grace_extension_period_granted = models.IntegerField()
    variable_quantity = models.IntegerField()
    sibling_bids = models.TextField()

class Vessel(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.OneToOneField(Bid)
    vessel_name = models.TextField()
    built = models.IntegerField(max_length=4,choices=YEARS)
    IMO_no = models.IntegerField()
    vessel_type = models.TextField()
    vessel_class = models.TextField()
    vessel_flag = models.IntegerField() #choice field with flag url and flag name
    GRT = models.IntegerField()
    NRT = models.IntegerField()
    LOA = models.IntegerField()
    BEAM = models.IntegerField()
    hold_hatches = models.IntegerField()
    dead_weight = models.IntegerField() # tonnes
    draft = models.IntegerField()
    TPC = models.IntegerField()
    cranes_spec = models.TextField()
    grabs_spec = models.TextField()
    speed_laden = models.IntegerField() #nautical miles
    speed_ballast = models.IntegerField()#nautical miles








class BidderNotification(models.Model):
    id = models.AutoField(primary_key=True)
    auction_id = models.ForeignKey(AuctionPost)
    bid_id = models.ForeignKey(Bid)
    auctioneer_id = models.ForeignKey(Auctioneer)
    bidder_id = models.ForeignKey(Bidder)
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    message = models.TextField(max_length=2000L)
