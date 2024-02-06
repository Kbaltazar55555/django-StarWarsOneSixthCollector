from django.urls import path
from .views import Home, SWList, SWDetail, CustomListCreate, CustomDetail 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sw/', views.SWList.as_view(), name='sw-list'),
    path('sw/<int:id>/', views.SWDetail.as_view(), name='sw-detail'),
    path('sw/<int:SW_id>/custom/', CustomListCreate.as_view(), name='custom-list-create'),
	  path('sw/<int:SW_id>/custom/<int:id>/', CustomDetail.as_view(), name='Custom-detail'),
]