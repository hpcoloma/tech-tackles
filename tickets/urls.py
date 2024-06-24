from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", include("tickets.urls"), name="tickets-urls"),
    # path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/comment/', views.add_comment, name='add_comment')
]

