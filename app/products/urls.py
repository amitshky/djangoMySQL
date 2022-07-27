from django.urls import URLPattern, URLResolver, path

from . import views


urlpatterns: list[URLPattern | URLResolver] = [
	path('', views.getProducts),
	path('<int:pk>/', views.getProductDetails),
	path('add/', views.addProduct),
	path('update/<int:pk>/', views.updateProduct),
	path('delete/<int:pk>/', views.deleteProduct),

	# using Class based API view
	path('class/', views.ProductListCreateAPIView.as_view()),              # POST to create, GET to list data
	path('class/<int:pk>/', views.ProductDetailAPIView.as_view()),         # GET
	path('class/update/<int:pk>/', views.ProductUpdateAPIView.as_view()),  # PUT
	path('class/delete/<int:pk>/', views.ProductDestroyAPIView.as_view()), # DELETE

	# using mixins
	path('mixins/', views.ProductMixinView.as_view()),
	path('mixins/<int:pk>/', views.ProductMixinView.as_view()),
]