from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from decimal import Decimal

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user =User.objects.create(**validated_data)
        user.save()
        return user

class EmailValidationSerializer(serializers.Serializer):
    email=serializers.CharField()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class ItemSalePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSalePrice
        fields = '__all__'

    # def to_representation(self, instance):
    #     # Get the original representation
    #     representation = super().to_representation(instance)

    #     # Check if the request is available and if the user is authenticated
    #     request = self.context.get('request')
    #     if  not request.user.is_authenticated:
    #         # Remove unit_price if the user is not authenticated
    #         representation.pop('unit_price', None)
    #         return representation
    #     else:
    #         return representation
    
class ItemSerializer(serializers.ModelSerializer):
    unit_price=serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = '__all__'

    def get_unit_price(self, obj):
        # Retrieve the request object from the serializer context
        request = self.context.get('request')
        user = request.user if request else None

        if user and user.is_authenticated:
            try:
                price = ItemSalePrice.objects.get(
                    item_no=obj.item_no,
                    salecode=user.customer.customer_price_group
                )
                return float(price.unit_price)
            except ItemSalePrice.DoesNotExist:
                return None
        return None
