from rest_framework import serializers

from .models import *


class DressSerializer(serializers.ModelSerializer):
    class Meta:

        model = Dress
        fields='__all__'


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'