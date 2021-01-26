from django.urls import path
from . import views

app_name = 'modules'
urlpatterns = [
    path('GetModules', views.api_get_modules),
]
