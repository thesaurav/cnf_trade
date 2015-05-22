__author__ = 'animesh'
from django.contrib.auth.models import User
from rest_framework import serializers
from bid.models import Bidder, Vessel, Bid


class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = (
            "id",
            "cargo_name",
            "category",
            "cargo_quantity",
            "variable_quantity",
            "load_port",
            "discharge_port",
            "max_bid_amount",
            "vessel_type",
            "origin_date_from",
            "origin_date_to",
            "destination_date_from",
            "destination_date_to",
            "other_requirements",
            "number_of_voyages",
            "load_rate",
            "discharge_rate",
            "description",
            "total_bids",
            "posted_on",
            "terms_conditions",


        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            "username",
            "first_name",
            "last_name",
            "email",
            "id"
        )

class BidderSerializer(serializers.ModelSerializer):
    user_details = UserSerializer()
    class Meta:
        model = Bidder
        fields = (
            "contact_person",
            "designation",
            "country",
            "city",
            "state",
            "pin_code",
            "registered_address",
            "phone_number",
            "fax",
            "email1",
            "organisation_name",
            "organisation_type",
            "latitude",
            "longitude",
            "business_activity",
            "total_posts",
            "user_details"
        )

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = (
            "vessel_name",
            "built",
            "IMO_no",
            "vessel_type",
            "vessel_class",
            "GRT",
            "NRT",
            "LOA",
            "BEAM",
            "hold_hatches",
            "dead_weight",
            "draft",
            "TPC",
            "cranes_spec",
            "grabs_spec",
            "speed_laden",
            "speed_ballast"
        )

