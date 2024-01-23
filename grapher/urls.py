from django.urls import path
from .views import chart_view

app_name = 'grapher'

urlpatterns = [
    path('chart/', chart_view, name='chart'),
]