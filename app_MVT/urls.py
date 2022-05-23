from django.urls import path

from app_MVT import views


urlpatterns = [
path('in_familia/<str:nombre>/<int:numero>/<fechaDeEntrega>', views.in_familia),
path('all_familia/', views.all_familia,name='all_familia'),
path('', views.index,name='index'),


]