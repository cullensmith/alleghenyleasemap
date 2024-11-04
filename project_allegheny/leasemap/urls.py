from django.urls import path
from . import views


app_name = 'leasemap'

urlpatterns = [
    path('',views.leasemap, name="leasemap"),
    path('parcels',views.parcels, name="parcels"),
    path('coordints',views.coordints, name="coordints"),
    path('filteredparcels',views.filteredparcels, name="filteredparcels"),
    path('polygon_geojson_view', views.polygon_geojson_view, name='polygon_geojson_view'),
    path('getMask', views.getMask, name='getMask'),
    path('get_matches', views.get_matches, name='get_matches'),
    path('get_wellsc', views.get_wellsc, name='get_wellsc'),
    path('get_wellsu', views.get_wellsu, name='get_wellsu'),

]