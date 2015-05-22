from django.shortcuts import render

from rest_framework import status
from bid.models import Bid

__author__ = 'animesh'

from .models import Auctioneer, AuctionPost
from .serializers import AuctioneerSerializer,AuctionPostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class AuctioneerUser(APIView):

    def get_object(self,id):
        try:
            return Auctioneer.objects.get(pk = id)
        except Auctioneer.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        user = self.get_object(id)
        serializer = AuctioneerSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuctioneerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        serializer = AuctioneerSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #TODO Auctioneer deletes account with active auction

class AuctionDetail(APIView):
    def get_object(self,id):
        try:
            return AuctionPost.objects.get(pd = id)
        except AuctionPost.DoesNotExist:
            raise Http404

    def get(self,request,id,format=None):
        post = self.get_object(id)
        serialised_post = AuctionPostSerializer(post)
        return Response(serialised_post.data)

    def put(self,request,id,format=None):
        post = self.get_object(id)
        serializer = AuctionPostSerializer(post,data=request.data)
        if request.user.id == post.user__id:
            if serializer.is_valid():
                bids = Bid.objects.get(post.id)
                if not bids:
                    serializer.save()
                else:
                    #TODO update only certain fields and all fields when no post has been made
                    pass
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_FORBIDDEN)

    def delete(self,request,id,format=None):
        post = self.get_object(id)
        if request.user.id == post.user__id:
            bids = Bid.objects.get(post.id)
            if not bids:
                post.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_401_FORBIDDEN)
