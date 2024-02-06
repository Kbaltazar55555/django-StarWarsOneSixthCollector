from django.urls import path
from .views import Home
from .views import Home, SWList, SWDetail 

urlpatterns = [
  path('', Home.as_view(), name='home'),
]

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('SW/', SWList.as_view(), name='SW-list'),
  path('SW/<int:id>/', SWDetail.as_view(), name='SW-detail'),
]