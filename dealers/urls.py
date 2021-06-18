from django.urls import path
from . import views

urlpatterns = [
    path('add_dealer', views.AddDealer.as_view(), name='add_dealer'),
    path('<slug:slud>/<slug:city_slug>/<int:pk>/', views.DealerDetailView.as_view(), name='dealer_detail'),
    path('<slug:slug>/<slug:city_slug>/', views.DealersListView.as_view(), name='site_list'),
    path('<slug:slug>/', views.DealersCityView.as_view(), name='dealers_by_brand'),
    path('', views.DealersBrandView.as_view(), name='brands_list'),
]
