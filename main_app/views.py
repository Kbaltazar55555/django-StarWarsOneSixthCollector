from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import SW, Custom, Vehicle
from .serializers import SWSerializer, CustomSerializer, VehicleSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the StarWarscollector api home route!'}
    return Response(content)

class SWList(generics.ListCreateAPIView):
    queryset = SW.objects.all()
    serializer_class = SWSerializer

class SWDetail(generics.RetrieveUpdatesDestroyAPIView):
   queryset = SW.objects.all()
   serializer_class = SWSerializer
   lookup_field = 'id'


class CustomListCreate(generics.ListCreateAPIView):
   serializer_class = CustomSerializer

   def get_queryset(self):
      SW_id = self.kwargs['SW_id']
      return Custom.objects.filter(SW_id=SW_id)
   
   def perform_create(self, serializer):
      SW_id = self.kwargs['SW_id']
      SW = SW.objects.get(id=SW_id)
      serializer.save(SW=SW)

class CustomDetail(generics.RetrieveUpdateDestroyAPIView):
   
   serializer_class = CustomSerializer
   lookup_field = 'id'

   def get_queryset(self):
      SW_id = self.kwargs['SW_id']
      return Custom.objects.filter(SW_id=SW_id)
   
class VehicleList(generics.ListCreateAPIView):
  queryset = Vehicle.objects.all()
  serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Vehicle.objects.all()
  serializer_class = VehicleSerializer
  lookup_field = 'id'
   
   