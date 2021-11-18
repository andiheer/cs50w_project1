from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Entry view
    path('wiki/<str:title>', views.view_entry, name="entry"),
    path('edit/<str:title>', views.edit_entry, name="edit entry"),
]
