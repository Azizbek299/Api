from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView


def home(request):
    return render(request, 'softapp/home.html')


class BoglanishApi(ListCreateAPIView):
    queryset = Boglanish.objects.all()
    serializer_class = BoglanishSerializer


class BoglanishApiView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        boglanish = Boglanish.objects.all()
        serializer = BoglanishSerializer(boglanish, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoglanishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        phone_number = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(phone_number, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoglanishDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Boglanish.objects.get(pk=pk)
        except Boglanish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        boglanish = Boglanish.objects.get(pk=pk)
        serializer = BoglanishSerializer(boglanish)
        return Response(serializer.data)

    def put(self, request, pk):
        boglanish = Boglanish.objects.get(pk=pk)
        serializer = BoglanishSerializer(boglanish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        boglanish = Boglanish.objects.get(pk=pk)
        boglanish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhoneDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return PhoneNumber.objects.get(pk=pk)
        except PhoneNumber.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        phone = PhoneNumber.objects.get(pk=pk)
        serializer = PhoneNumberSerializer(phone)
        return Response(serializer.data)

    def put(self, request, pk):
        phone = PhoneNumber.objects.get(pk=pk)
        serializer = PhoneNumberSerializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        phone = PhoneNumber.objects.get(pk=pk)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SimpleCreateListApiView(ListCreateAPIView):
    queryset = Boglanish.objects.all()
    serializer_class = BoglanishSerializer


class SimpleUdateView(UpdateAPIView):
    queryset = Boglanish.objects.all()
    serializer_class = BoglanishSerializer
    lookup_field = 'id'
