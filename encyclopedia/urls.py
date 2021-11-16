from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Entry view
    path('<str:title>/', views.view_entry, name="entry")
]
