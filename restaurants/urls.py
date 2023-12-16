from django.urls import path
from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
    RestaurantDeleteView,
    MyPostView
)
from django.contrib.auth.views import LoginView, LogoutView
from registration.backends.default.views import RegistrationView
from .views import custom_logout
urlpatterns = [
    path('accounts/logout/', custom_logout, name='custom_logout'),

    path('register/', RegistrationView.as_view(), name='registration_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('', RestaurantListView.as_view(), name='home'),
    path('create/', RestaurantCreateView.as_view(), name='create'),
    path('<slug:slug>/', RestaurantDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', RestaurantUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', RestaurantDeleteView.as_view(), name='delete'),
    path('dashboard/myposts/', MyPostView.as_view(), name='my_posts'),
    path('category/<str:category_slug>/', RestaurantListView.as_view(), name='restaurant_list_by_category'),
    

]
