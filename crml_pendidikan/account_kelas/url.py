from django.urls import path
from . import views

urlpatterns = [
	# path ('',views.home),
	# path ('products/',views.products),
	# path ('customer/',views.customer
    path('', views.index, name='home'),
    path('products/', views.index, name='products'),
    path('customer/', views.index, name='customer/')

]
