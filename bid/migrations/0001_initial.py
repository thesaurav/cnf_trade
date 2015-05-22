# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('auction_id', models.IntegerField()),
                ('contact_to_person_phone', models.IntegerField()),
                ('contact_to_person_name', models.TextField(default=None, max_length=50)),
                ('bid_time', models.DateTimeField(auto_now=True)),
                ('bid_price', models.FloatField()),
                ('bid_comment', models.TextField(max_length=255)),
                ('expected_voyage_start_date', models.DateTimeField(default=None)),
                ('origin', models.TextField(max_length=100)),
                ('destination', models.TextField(max_length=100)),
                ('terms_conditions', models.TextField(max_length=1000)),
                ('accepted_terms', models.TextField()),
                ('in_deal_phase', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_halted', models.BooleanField(default=False)),
                ('expected_voyage_end_date', models.DateTimeField()),
                ('grace_extension_period_granted', models.IntegerField()),
                ('variable_quantity', models.IntegerField()),
                ('sibling_bids', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('phone_number', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('is_dnd', models.BooleanField()),
                ('country', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=50)),
                ('city', models.TextField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('registered_address', models.TextField(max_length=100)),
                ('total_posts', models.IntegerField()),
                ('is_privileged', models.BooleanField(default=False)),
                ('email1', models.EmailField(max_length=254)),
                ('business_activity', models.TextField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('organisation_name', models.TextField(max_length=100)),
                ('organisation_type', models.TextField(max_length=100)),
                ('contact_person', models.TextField(max_length=100)),
                ('designation', models.TextField()),
                ('total_bids_made', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('vessel_name', models.TextField()),
                ('built', models.IntegerField(max_length=4, choices=[(1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('IMO_no', models.IntegerField()),
                ('vessel_type', models.TextField()),
                ('vessel_class', models.TextField()),
                ('vessel_flag', models.IntegerField()),
                ('GRT', models.IntegerField()),
                ('NRT', models.IntegerField()),
                ('LOA', models.IntegerField()),
                ('BEAM', models.IntegerField()),
                ('hold_hatches', models.IntegerField()),
                ('deadWeight', models.IntegerField()),
                ('draft', models.IntegerField()),
                ('TPC', models.IntegerField()),
                ('cranes_spec', models.TextField()),
                ('grabs_spec', models.TextField()),
                ('speed_laden', models.IntegerField()),
                ('speed_ballast', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(to='bid.Bidder'),
        ),
        migrations.AddField(
            model_name='bid',
            name='vessel',
            field=models.ForeignKey(to='bid.Vessel'),
        ),
    ]
