from django.urls import path
from cvmaker import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index/', views.IndexView.as_view(), name='index'),

    path('person_list/', views.PersonListView.as_view(), name='person_list'),
    path('person_create/', views.PersonCreateView.as_view(), name='person_create'),
    path('person_detail/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),

]