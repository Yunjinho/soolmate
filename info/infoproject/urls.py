from django.contrib import admin
from django.urls import path
import infoapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', infoapp.views.index, name="index"),
]
