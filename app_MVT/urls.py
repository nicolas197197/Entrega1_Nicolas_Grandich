from django.urls import path

from app_MVT import views


urlpatterns = [
path('in_futbol/<str:nombre>/<int:numero>/<fechaDeIngreso>', views.in_futbol),
path('', views.index,name='inicio'),
path('futbol/', views.futbol,name='futbol'),
path('futbol-django-forms', views.futbol_forms_django, name='FutbolDjangoForms'),
path('basquet-django-forms', views.basquet_forms_django, name='BasquetDjangoForms'),
path('basquet/', views.basquet,name='basquet'),
path('tenis-django-forms', views.tenis_forms_django, name='TenisDjangoForms'),
path('tenis/', views.tenis,name='tenis'),
path('search', views.search, name='Search'),


]