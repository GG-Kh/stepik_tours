from django.urls import path

from tours import views

urlpatterns = [
    path(
        'departure/<str:departure>/',
        views.DepartureView.as_view(),
        name='departure'
        ),
    path('tour/<int:id>/', views.TourView.as_view(), name='tour'),
]
