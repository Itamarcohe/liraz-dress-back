from django.urls import path

from . import views



urlpatterns = [
    path('dresses',views.getAllDress),
    path('contact_us',views.contact_us),
    path('order',views.make_order)
]

