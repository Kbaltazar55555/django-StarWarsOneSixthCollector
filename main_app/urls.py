from django.urls import path
from .views import Home, SWList, SWDetail, CustomListCreate, CustomDetail, VehicleList, VehicleDetail, AddVehicleToSW, RemoveVehicleFromSW

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sw/', SWList.as_view(), name='sw-list'),
    path('sw/<int:id>/', SWDetail.as_view(), name='sw-detail'),
    path('sw/<int:SW_id>/custom/', CustomListCreate.as_view(), name='custom-list-create'),
	  path('sw/<int:SW_id>/custom/<int:id>/', CustomDetail.as_view(), name='Custom-detail'),
    path('vehicle/', VehicleList.as_view(), name='vehicle-list'),
    path('vehicle/<int:id>/', VehicleDetail.as_view(), name='vehicle-detail'),
    path('vehicle/<int:id>/add_vehicle/', AddVehicleToSW.as_view(), name='add-vehicle-to-sw'),
    path('vehicle/<int:id>/remove_vehicle/', RemoveVehicleFromSW.as_view(), name='remove-vehicle-from-sw'),
]