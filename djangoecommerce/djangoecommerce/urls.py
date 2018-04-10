from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
	path('', views.index, name='index'),	
	path('catalogo/', include('catalog.urls', namespace='catalog')),	
	path('contato/', views.contact, name='contact'),	
    path('admin/', admin.site.urls),
]
