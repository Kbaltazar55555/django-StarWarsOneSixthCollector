from django.urls import path
from .views import Home, SWList, SWDetail, CustomListCreate, CustomDetail, VehicleList, VehicleDetail, AddVehicleToSW, RemoveVehicleFromSW

urlpatterns = [
    path('', Home.as_view(), name='home'), #works
    path('sw/', SWList.as_view(), name='sw-list'), #works
    path('sw/<int:id>/', SWDetail.as_view(), name='sw-detail'), #works
    path('sw/<int:sw_id>/custom/', CustomListCreate.as_view(), name='custom-list-create'), #works
    path('sw/<int:sw_id>/custom/<int:id>/', CustomDetail.as_view(), name='custom-detail'),
    path('vehicle/', VehicleList.as_view(), name='vehicle-list'), #works
    path('vehicle/<int:id>/', VehicleDetail.as_view(), name='vehicle-detail'), #works
    path('sw/<int:sw_id>/vehicle/<int:vehicle_id>/add_vehicle/', AddVehicleToSW.as_view(), name='add-vehicle-to-sw'),
    path('sw/<int:sw_id>/vehicle/<int:vehicle_id>/remove_vehicle/', RemoveVehicleFromSW.as_view(), name='remove-vehicle-from-sw'),
]