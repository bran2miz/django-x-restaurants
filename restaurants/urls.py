from django.urls import path
from .views import RestaurantsListView, RestaurantsDetailView, RestaurantsCreateView, RestaurantsUpdateView, RestaurantsDeleteView

urlpatterns = [
    path('', RestaurantsListView.as_view(), name='restaurants_list'),
    path('<int:pk>/', RestaurantsDetailView.as_view(), name='restaurants_detail'),
    path('create/', RestaurantsCreateView.as_view(), name='restaurants_create'),
    path('<int:pk>/update/', RestaurantsUpdateView.as_view(), name='restaurants_update'),
    path('<int:pk>/delete/', RestaurantsDeleteView.as_view(), name='restaurants_delete'),
]