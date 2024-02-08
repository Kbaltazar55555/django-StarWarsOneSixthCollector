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

class SWDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = SW.objects.all()
   serializer_class = SWSerializer
   lookup_field = 'id'

   def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    Vehicles_not_associated = Vehicle.objects.exclude(id__in=instance.vehicles.all())
    Vehicles_serializer = VehicleSerializer(Vehicles_not_associated, many=True)

    return Response({
        'sw': serializer.data,
        'Vehicles_not_associated': Vehicles_serializer.data
    })


class CustomListCreate(generics.ListCreateAPIView):
   serializer_class = CustomSerializer

   def get_queryset(self):
      SW_id = self.kwargs['sw_id']
      return Custom.objects.filter(sw_id=sw_id)
   
   def perform_create(self, serializer):
      SW_id = self.kwargs['sw_id']
      SW = SW.objects.get(id=sw_id)
      serializer.save(sw=sw)

class CustomDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Custom.objects.all()
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
   
class AddVehicleToSW(APIView):
    def post(self, request, sw_id, vehicle_id):
        sw = SW.objects.get(id=sw_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)
        sw.vehicles.add(vehicle)
        return Response({'message': f'Vehicle {vehicle.name} added to SW {sw.name}'})

class RemoveVehicleFromSW(APIView):
  def post(self, request, sw_id, vehicle_id):
    sw = SW.objects.get(id=sw_id)
    vehicle = Vehicle.objects.get(id=vehicle_id)
    sw.vehicles.remove(vehicle)
    return Response({'message': f'Vehicle {vehicle.name} removed from SW {sw.name}'})