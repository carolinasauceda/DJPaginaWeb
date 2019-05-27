from django.urls import path
from django.conf.urls import url
from . import views
from .views import *


urlpatterns = [
    path("",views.menu,name='Menu principal'),
    path("tienda/",views.shop,name='Tienda'),
    url('detalles/(?P<codigo>\d+)/$',views.detalles ,name='Detalles'),
    url('compra/(?P<code>\d+)/$',views.formulario,name='registro'),
    url('pago/(?P<code>\d+)/$/(?P<user>\d+)/$',views.pago,name='Pago'),

]