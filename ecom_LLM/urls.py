from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add_ten/<str:question>/', views.add_ten, name='add_ten'),
]
