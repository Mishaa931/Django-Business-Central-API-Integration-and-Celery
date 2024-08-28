# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
from .models import *
from .serializers import *
from django.apps import apps
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class EmailValidationView(APIView):
    serializer_class=EmailValidationSerializer
    def post(self, request):
        customer_email = request.data.get('email')
        if not customer_email:
            return Response({'error': 'Email address is required'}, status=status.HTTP_400_BAD_REQUEST)
        queryset=Customer.objects.filter(email=customer_email)
        serializer=EmailValidationSerializer(queryset,many=True)
        if queryset.exists():
            request.session['customer_email']=customer_email
            request.session.modified = True  # Ensure session is saved
            print(f"Session email set: {request.session.get('customer_email')}")  # Debugging statement            print("The email exists",serializer.data)
            return Response({
                'message': 'Your email address exists.You can signup now.',
                'data':serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email address is not associated with any customer'}, status=status.HTTP_404_NOT_FOUND)



class SignupAPIView(generics.CreateAPIView):
  queryset=User.objects.all()
  serializer_class = RegisterSerializer

  def create(self,request):
    customer_email = request.session.get('customer_email')
    print("customer_email",customer_email)
        
    if customer_email:
        copied_data = request.data.copy() #making mutable copy of QueryDict
        print("data before adding email:", copied_data)  
        copied_data['email'] = customer_email  
        print("data after adding email:", copied_data['email'])  
    else:
        return Response({'error': 'Validated email not found'}, status=status.HTTP_400_BAD_REQUEST)

    if  copied_data['email']!=customer_email:
        return Response({'error':'Email does not match validated email'})
    
    serializer=RegisterSerializer(data=copied_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("email")
        print("username",username)  
        password = request.data.get("password")
        print("password",password)
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return Response("Login successful", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Invalid user", status=status.HTTP_400_BAD_REQUEST)

   

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    # queryset = Customer.objects.all()
    serializer_class =CustomerSerializer 
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = "__all__"
    search_fields = "__all__"

    def get_queryset(self):
        self.user_email=self.request.user.email
        print("user_email", self.user_email)
        queryset=Customer.objects.filter(email=self.user_email)
        print("customer email",queryset)
        return queryset
    
    def list(self,request):
        queryset=self.get_queryset()
        print("list queryset",queryset)
        if queryset.exists():
            print("email addresses are same.")
            print("QuerySet data:", queryset.values())
            serializer=self.get_serializer(queryset, many=True)
            print(serializer.data)
            return Response(serializer.data)
        
        else:
            print("your email address is not valid")
            return Response(
                {"detail": "Your email address is not authorized to view this data."},
                status=status.HTTP_403_FORBIDDEN
            )

    

class ItemSalePriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = ItemSalePrice.objects.all()
    serializer_class =ItemSalePriceSerializer 
    # pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = "__all__"
    search_fields = "__all__"

    def get_permissions(self):
        if self.action in ['list']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_authenticated:
            try:
                customer = user.customer
                customer_price_group = customer.customer_price_group
                return ItemSalePrice.objects.filter(salecode=customer_price_group)
            except AttributeError:
                # Handle case where user might not have a related customer object
                return ItemSalePrice.objects.none()
        else:
            # Allow unauthenticated users to see data
            return ItemSalePrice.objects.all()
        

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class =ItemSerializer 
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = "__all__"
    search_fields = "__all__"

    def get_permissions(self):
        if self.action in ['list']:
            return[AllowAny()]
        return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        # Pass the request context to the serializer
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})

        page = self.paginate_queryset(serializer.data)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(serializer.data)

        
