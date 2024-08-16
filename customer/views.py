from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerAPIView(APIView):

    @extend_schema(
        summary="Get all customers",
        description="Get all customers in the system",
        responses={200: CustomerSerializer(many=True)}
    )
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Create a customer",
        description="Create a new customer",
        request=CustomerSerializer,
        responses={201: CustomerSerializer}
    )
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailAPIView(APIView):

    @extend_schema(
        summary="Get a customer",
        description="Get a customer by ID",
        responses={200: CustomerSerializer}
    )
    def get(self, request, id):
        customer = Customer.objects.get(pk=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    @extend_schema(
        summary="Update a customer",
        description="Update a customer by ID",
        request=CustomerSerializer,
        responses={200: CustomerSerializer}
    )
    def put(self, request, id):
        customer = Customer.objects.get(pk=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Delete a customer",
        description="Delete a customer by ID",
        responses={204: None}
    )
    def delete(self, request, id):
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
