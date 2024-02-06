from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import SW

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