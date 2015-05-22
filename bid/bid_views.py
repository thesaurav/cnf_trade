__author__ = 'animesh'

# Create your views here.
from rest_framework import status
from .models import Bidder,BidderNotification,Bid
from .serializers import BidderSerializer, BidSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class BidderUser(APIView):

    def get_object(self,id):
        try:
            return Bidder.objects.get(pk = id)
        except Bidder.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        user = self.get_object(id)
        serializer = BidderSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BidderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        serializer = BidderSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#TODO - Bidder deleted account with active bids