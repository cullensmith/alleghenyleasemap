from django.urls import path
from . import views


app_name = 'leasemap'

urlpatterns = [
    path('',views.leasemap, name="leasemap"),
    path('parcels',views.parcels, name="parcels"),
    path('coordints',views.coordints, name="coordints"),
    path('filteredparcels',views.filteredparcels, name="filteredparcels"),
    path('getMask', views.getMask, name='getMask'),
    path('get_matches', views.get_matches, name='get_matches'),
]