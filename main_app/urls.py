from django.urls import path
from .views import Home, SWList, SWDetail, CustomListCreate, CustomDetail, VehicleList, VehicleDetail, AddVehicleToSW

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sw/', SWList.as_view(), name='sw-list'),
    path('sw/<int:id>/', SWDetail.as_view(), name='sw-detail'),
    path('sw/<int:SW_id>/custom/', CustomListCreate.as_view(), name='custom-list-create'),
	  path('sw/<int:SW_id>/custom/<int:id>/', CustomDetail.as_view(), name='Custom-detail'),
    path('vehicle/', VehicleList.as_view(), name='vehicle-list'),
    path('toys/<int:id>/', VehicleDetail.as_view(), name='vehicle-detail'),
    path('sw/<int:sw_id>/add_vehicle/<int:vehicle_id>/', AddVehicleToSW.as_view(), name='add-vehicle-to-sw'),
    path('sw/<int:sw_id>/remove_vehicle/<int:vehicle_id>/', RemoveVehicleFromSW.as_view(), name='remove-vehicle-from-sw'),
]