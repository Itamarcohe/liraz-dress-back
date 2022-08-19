from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from liraz_app.serializers import *


@api_view(['GET'])
def getAllDress(request):
    all_dresses = Dress.objects.all()
    serializer = DressSerializer(all_dresses,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def contact_us(request):
    if request.method == 'GET':
        all_leads = Lead.objects.all()
        serializer = LeadSerializer(all_leads,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        new_lead = Lead.objects.create(
            full_name=request.data['full_name'],
            phone_number=request.data['phone_number'],
            email=request.data['email'],
            description=request.data['description']
        )
        new_lead.save()
        return Response('Created!')

@api_view(['POST'])
def make_order(request):
    if request.method == 'POST':
        order_details = request.data
        new_order = Order.objects.create(
            customer_name=order_details['customer_name'],
            phone_number=order_details['phone_number'],
            top_item=order_details['top_item'],
            back_item=order_details['back_item'],
            bottom_item=order_details['bottom_item'],
            color=order_details['color']
        )
        new_order.save()
        serializer = OrderSerializer(new_order,many=False)
        return Response(serializer.data)


# Create your views here.
