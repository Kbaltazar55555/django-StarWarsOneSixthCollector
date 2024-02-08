from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions # modify these imports to match
from django.http import Http404
from .models import SW, Custom, Vehicle
from .serializers import SWSerializer, CustomSerializer, VehicleSerializer, UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied # include this additional import


# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the StarWarscollector api home route!'}
    return Response(content)

class SWList(generics.ListCreateAPIView):
    queryset = SW.objects.all()
    serializer_class = SWSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
      # This ensures we only return cats belonging to the logged-in user
      user = self.request.user
      return SW.objects.filter(user=user)

    def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)


class SWDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = SW.objects.all()
   serializer_class = SWSerializer
   lookup_field = 'id'
   
   def get_queryset(self):
    user = self.request.user
    return SW.objects.filter(user=user)

   def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    Vehicles_not_associated = Vehicle.objects.exclude(id__in=instance.vehicles.all())
    Vehicles_serializer = VehicleSerializer(Vehicles_not_associated, many=True)

    return Response({
        'sw': serializer.data,
        'Vehicles_not_associated': Vehicles_serializer.data
    })

    def perform_update(self, serializer):
      sw = self.get_object()
      if sw.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this figure."})
    serializer.save()

    def perform_destroy(self, instance):
      if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this figure."})
    instance.delete()


class CustomListCreate(generics.ListCreateAPIView):
    serializer_class = CustomSerializer

    def get_queryset(self):
        # Ensure variable names are consistent
        sw_id = self.kwargs['sw_id']  # Use lower case to match URL parameter
        return Custom.objects.filter(sw_id=sw_id)
   
    def perform_create(self, serializer):
        sw_id = self.kwargs['sw_id']  # Ensure this matches the URL parameter
        sw = SW.objects.get(id=sw_id)  # Correct variable usage
        serializer.save(sw=sw)



class CustomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Custom.objects.all()
    serializer_class = CustomSerializer
    lookup_field = 'id'

    def get_object(self):
        # Directly get the object using the built-in mechanism
        obj = super().get_object()  # This automatically uses 'id' from the URL

        # Safely get 'sw_id' from the URL parameters
        sw_id = self.kwargs.get('sw_id')

        # Verify if 'sw_id' matches the Custom object's associated SW id
        if sw_id and obj.sw.id != int(sw_id):
            raise Http404("No Custom object found matching the SW id and Custom id.")

        return obj
   
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
  
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })