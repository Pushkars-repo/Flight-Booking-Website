from django.contrib import admin
from django.urls import path
from . import views
# from .views import UserRegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('flight_detail_page', views.flight_detail_page, name='flight_detail_page'),
    path('search_flight_details', views.search_flight_details, name='search_flight_details'),
    path('book_ticket/<int:id>', views.book_ticket, name='book_ticket'),
    path('confirm_tkt/<int:id>', views.confirm_tkt, name='confirm_tkt'),

    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]
