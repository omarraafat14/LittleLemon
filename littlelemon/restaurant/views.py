from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from .serializers import *


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# class BookingView(APIView): 
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data) # return JSON

#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemView(ListCreateAPIView): 
    serializer_class = MenuSerializer
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data) # return JSON

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer
    def get(self, request, pk):
        item = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(item)
        return Response(serializer.data) # return JSON

    def delete(self, request, pk):
        item = Menu.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 