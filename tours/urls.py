from django.urls import path
from tours import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('departure/<str:departure>/', views.DepartureView.as_view()),
    path('tour/<int:id>/', views.TourView.as_view()),
]
