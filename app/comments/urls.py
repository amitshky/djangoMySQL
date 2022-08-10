from django.urls import URLPattern, URLResolver, path

from . import views

urlpatterns: list[URLPattern | URLResolver] = [
	path('', views.comments),
	path('<int:pk>/', views.comments),
]