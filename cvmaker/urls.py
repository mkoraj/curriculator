from django.urls import path
from cvmaker import views


urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
]