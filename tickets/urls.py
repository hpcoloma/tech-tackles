import django.urls import path, include
form django.contrib import admin
from . import views

urlpatterns = [
    path("", include("tickets.urls"), name="tickets-urls"),
    path('tickets/<int:ticket_id>/comment/', views.add_comment, name='add_comment')
]

